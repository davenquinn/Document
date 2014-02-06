// Generated on 2013-11-11 using generator-webapp 0.4.4
'use strict';

// # Globbing
// for performance reasons we're only matching one level down:
// 'test/spec/{,*/}*.js'
// use this if you want to recursively match all subfolders:
// 'test/spec/**/*.js'

module.exports = function (grunt) {
    // show elapsed time at the end
    require('time-grunt')(grunt);
    // load all grunt tasks
    require('load-grunt-tasks')(grunt);

    grunt.initConfig({
        // configurable paths
        doc: grunt.file.readJSON('document/config.json'),
        copy: {
            dist: {
                files: [{
                    expand: false,
                    dot: false,
                    cwd: '.build',
                    dest: 'dist',
                    src: [
                        '*.{pdf,html}'
                    ]
                }]
            }
        }
    });

    grunt.registerTask('make', [
        'copy:dist',
    ]);

    grunt.registerTask('build', [
        'clean:dist',
        'useminPrepare',
        'concurrent:dist',
        'autoprefixer',
        'concat',
        'cssmin',
        'uglify',
        'modernizr',
        'copy:dist',
        'rev',
        'usemin'
    ]);

    grunt.registerTask('default', [
        'jshint',
        'test',
        'build'
    ]);
};
