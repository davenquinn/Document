// Generated on 2013-11-11 using generator-webapp 0.4.4

module.exports = function (grunt) {
    // show elapsed time at the end
    require('time-grunt')(grunt);
    // load all grunt tasks
    require('load-grunt-tasks')(grunt);

    var options = grunt.file.readJSON('document/config.json')

    grunt.initConfig({
        // configurable paths
        doc: options,
        exec: {
            text: {
                // before even going to theme, replace things from within text files
                cmd: function() {
                    if (options.cite_backend == "biber") {t = "--biblatex"}
                    else {t = "--natbib"}
                    console.log(t)
                    return 'components/scripts/figures.py document/text/main.md | pandoc -t latex '+t+' -o .build/main.tex';
                }
            },
            bib: {
                cmd: function() {
                    if (options.cite_backend == "biber") {return "biber .build/skeleton";}
                    else { return "bibtex8 .build/skeleton.aux"}
                }
            },
            preprocess: {
                cmd: function() {
                    return "components/scripts/replace.py components/lib/"+options.theme+"/latex/skeleton.tex > .build/skeleton.tex"
                }
            },
            latex: {
                cmd: function(){
                    return "xelatex -output-directory .build .build/skeleton.tex";
                }
            },
            move: {
                cmd: function() {
                    return "mv .build/skeleton.pdf dist/"+options.filename;
                }
            }
        }
    });

    grunt.registerTask('make', [
        'exec:text',
        'exec:preprocess',
        'exec:latex',
        'exec:bib',
        'exec:latex',
        'exec:move'
    ]);
};
