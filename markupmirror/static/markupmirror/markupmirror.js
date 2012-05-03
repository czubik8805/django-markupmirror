var markupmirror = {
    "jQuery": jQuery
};

(function($) {
    $(function() {

        var MarkupMirrorEditor = function( element, options ) {
                    var _this = this,
                        _public = {

                            /* to configure the wrapper */
                            configure: function( obj ) {
                                for( key in obj ) {
                                    _private.options[ key ] = obj[ key ];
                                }

                                return _this;
                            },

                            get: function( key ) {
                                return _private.options[ key ] || undefined;
                            },

                            /* add the Codemirror to a new element */
                            add: function( el, options ) {
                                    if( !el || el.length === 0 ) {
                                        return _this;
                                    }

                                    var editor;

                                     $.each( el,
                                            function() {
                                                if( this.nodeName.toLowerCase() === 'textarea' ) {
                                                    if( options === undefined ) {
                                                        if( _private.getOption( '_init' ) === true && _private.getOption( 'inherit' ) === true ) {
                                                            editor = CodeMirror.fromTextArea( this, _private.getOption( 'initOptions' ) );
                                                            _public.configure( { 'editor': editor } );
                                                        } else {
                                                            editor = CodeMirror.fromTextArea( this );
                                                            _public.configure( { 'editor': editor } );
                                                        }
                                                    } else {

                                                        /* so we are able to overwrite just a few of the options */
                                                        if(  _private.getOption( '_init' ) === true && _private.getOption( 'extend' ) ) {
                                                            options = $.extend( _private.getOption( 'initOptions' ), options );
                                                        }

                                                        editor = CodeMirror.fromTextArea( this, options );
                                                        _public.configure( { 'editor': editor } );
                                                    }

                                                    if( typeof( _private.getOption( 'onInit' ) ) === 'function' ) {
                                                         _private.getOption( 'onInit' )( this );
                                                    }
                                                }
                                            });

                                    return _this;
                                 }
                        },

                        /* this will not be exposed to the public */
                        _private = {
                            getOption: function( index ) {
                                return _private.options[ index ] || undefined;
                            },

                            /* store configuration options here */
                            options: {
                                /* initial options passed in */
                                initOptions: undefined,

                                /* new added elements inherit from the inital options */
                                inherit: true,

                                /* extends the original options object by passing a new element in */
                                extend: true,

                                /* initial init was done */
                                _init: false,

                                /* callback */
                                onInit: undefined,

                                /* the original codemirror editor object */
                                editor: undefined
                            }
                        };

                    /* initialise the plugin here */
                    _public.configure( { _init: true,
                                         initOptions: options } );

                    /* add init element */
                    _public.add( element, options );

                    return _this = _public;
                };


        var $textarea = $('.item-markupmirror'),
            CM = new MarkupMirrorEditor( undefined, $textarea.data('mmSettings') )
                        .configure({'onInit': createIframe})
                        .configure({'onChange': updateIframe})
                        .add( $textarea );

                /* when init a textarea with codemirror we also create an iframe */
                function createIframe( el ) {
                    var $el = $(el),
                        $iframe = $('<iframe />').attr('src', $el.data('mmSettings')['base_url']);

                    $el.on('change', updateIframe);

                    $iframe
                    .insertAfter( $el );
                }

                /* when changing the textarea we replace the iframe content with the new coming from the server */
                function updateIframe( e ) {
                    console.log('update');
                }

            console.log( CM.get('editor') );

    });
})(markupmirror.jQuery);
