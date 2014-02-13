// Generated on 2013-11-11 using generator-webapp 0.4.4
'use strict';

module.exports = function (grunt) {
    // show elapsed time at the end
    require('time-grunt')(grunt);
    // load all grunt tasks
    require('load-grunt-tasks')(grunt);

    grunt.initConfig({
        // configurable paths
        doc: grunt.file.readJSON('document/config.json'),
        exec: {
            text: {
                // before even going to theme, replace things from within text files
                cmd: function() {
                    return 'components/scripts/figures.py document/text/main.md | pandoc -t latex --biblatex -o .build/main.tex';
                }
            },
            bib: {
                cmd: function() {
                    return "biber .build/skeleton";
                    //return "bibtex8 .build/skeleton.aux"
                }
            },
            preprocess: {
                cmd: function() {
                    return "components/scripts/replace.py components/lib/naturelike/latex/skeleton.tex > .build/skeleton.tex"
                }
            },
            latex: {
                cmd: function(){
                    return "xelatex -output-directory .build .build/skeleton.tex";
                }
            },
            move: {
                cmd: function() {
                    return "mv .build/skeleton.pdf dist/final.pdf";
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
