document.addEventListener("DOMContentLoaded", function() {

    var scanlines = $('.scanlines');
    var tv = $('.tv');
    function exit() {
        $('.tv').addClass('collapse');
        term.disable();
    }

    var __EVAL = (s) => eval(`void (__EVAL = ${__EVAL}); ${s}`);
    
    var term = $('#terminal').terminal(function(command, term) {
        var cmd = $.terminal.parse_command(command);


        if (cmd.name === 'exit') {
            exit();
        } else if (cmd.name === 'echo') {
            term.echo(cmd.rest);


        } else if (command !== '') {
            //Uncomment the below to allow for running actual js in term

            // try {
            //     var result = __EVAL(command);
            //     if (result && result instanceof $.fn.init) {
            //         term.echo('<#jQuery>');
            //     } else if (result && typeof result === 'object') {
            //         tree(result);
            //     } else if (result !== undefined) {
            //         term.echo(new String(result));
            //     }
            // } catch(e) {
            //     term.error(new String(e));
            // }
        }
    }, 
    
    {
        name: 'heyerappterm',
        onResize: set_size,
        exit: false,
        
        enabled: $('body').attr('onload') === undefined,
        onInit: function() {
            //WHEN TERMINAL IS FIRST INITIALIZED
            
            set_size();
            // this.echo('Type [[b;#fff;]exit] to see turn off animation.');
            // this.echo('Type and execute [[b;#fff;]grab()] function to get the scre' +
            //           'enshot from your camera');
            // this.echo('Type [[b;#fff;]camera()] to get video and [[b;#fff;]pause()]/[[b;#fff;]play()] to stop/play');
        },
        
        onClear: function() {
            console.log(this.find('video').length);
            this.find('video').map(function() {
                console.log(this.src);
                return this.src;
            });
        },
        prompt: 'HeyerApp> '
    });

    function set_size() {
        // for window height of 170 it should be 2s
        var height = $(window).height();
        var width = $(window).width()
        var time = (height * 2) / 170;
        scanlines[0].style.setProperty("--time", time);
        tv[0].style.setProperty("--width", width);
        tv[0].style.setProperty("--height", height);
    }
    
    function tree(obj) {
        term.echo(treeify.asTree(obj, true, true));
    }



    


    function clear() {
        term.clear();
    }


});