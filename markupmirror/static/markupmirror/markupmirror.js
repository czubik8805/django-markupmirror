var markupmirror = {
    "jQuery": jQuery
};

/* jQuery closure and document ready */
(function($) { $(function() {



/* make AJAX requests work with Django's CSRF protection */
$.ajaxSetup({
    crossDomain: false
});
$(document).ajaxSend(function(event, xhr, settings) {
    if (!(/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type))) {
        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    }
});


/* Plugin that handles the initialization of CodeMirror editors
   and preview iframes for each textarea.markupmirror-editor */
var MarkupMirrorEditor = function( element, options ) {
    var _this = this,
        _public = {

            /* to configure the wrapper */
            configure: function( obj ) {
                var key;
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

                /* skip if no element passed */
                if( !el || el.length === 0 ) {
                    return _this;
                }

                var editor;
                $.each( el, function() {
                    if( this.nodeName.toLowerCase() !== 'textarea' ) {
                        return true;
                    }

                    if( options === undefined ) {
                        if( _private.getOption( '_init' ) === true &&
                            _private.getOption( 'inherit' ) === true ) {
                            editor = CodeMirror.fromTextArea(
                                this,
                                _private.getOption( 'initOptions' ) );
                            _public.configure( { 'editor': editor } );
                        } else {
                            editor = CodeMirror.fromTextArea( this );
                            _public.configure( { 'editor': editor } );
                        }
                    } else {
                        /* so we are able to overwrite just a few of the
                         * options */
                        if( _private.getOption( '_init' ) === true &&
                            _private.getOption( 'extend' ) ) {
                            options = $.extend(
                                _private.getOption( 'initOptions' ),
                                options );
                        }

                        editor = CodeMirror.fromTextArea( this, options );
                        _public.configure( { 'editor': editor } );
                    }

                    if( typeof( _private.getOption( 'onInit' ) ) ===
                            'function' ) {
                        _private.getOption( 'onInit' )( this );
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

                /* extends the original options object by passing
                   a new element in */
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

    _this = _public;
    return _this;
};


/* initialize plugin for all textarea.markupmirror-editor elements */
var preview_delay,
    $textarea = $( '.markupmirror-editor' ),
    CM = new MarkupMirrorEditor( undefined,
            $.extend( {
                'onChange': function( editor ) {
                    clearTimeout( preview_delay );
                    preview_delay = setTimeout(function() {
                        updatePreview(editor);
                    }, 500);
                }
            },
            $textarea.data('mmSettings') ) )
        .configure({
            'onInit': createIframe
        })
        .add( $textarea );


/* when changing the textarea we replace the iframe content with the
   new coming from the server */
function updatePreview( editor ) {
    var $textarea = $( editor.getTextArea() ),
        $codemirror = $textarea.next( '.CodeMirror' ),
        $iframe = $codemirror.children( 'iframe' ),
        mm_settings = $textarea.data( 'mmSettings' ),
        url = mm_settings[ 'preview_url' ],
        markup_type = mm_settings[ 'markup_type' ];

    $.post(url, {
            /* csrfmiddlewaretoken: '{{ csrf_token }}', */
            markup_type: markup_type,
            text: editor.getValue()
        },
        function(data, textStatus, jqXHR) {
            $iframe.trigger('_resize');

            if( $iframe.data('load') === true ) {
                $iframe.trigger('_update',
                                {html: data});
            } else {
                $iframe.data('replace', data);
            }
        }
    );
}


/* when init a textarea with codemirror we also create an iframe */
function createIframe( textarea ) {
    var $textarea = $( textarea ),
        $iframe = $( '<iframe />' ).attr(
            'src', $textarea.data( 'mmSettings' )[ 'base_url' ] ),
        $codemirror = $textarea.next( '.CodeMirror' );

    $iframe
        .addClass( 'CodeMirror-preview' )
        .on({
            'load': function() {
                var $this = $(this);
                $this.data('load', true);

                if( $this.data('replace') !== undefined ) {
                    $this.trigger(
                        '_update',
                        {html: $this.data('replace')});
                }
            },
            '_resize': function() {
                $(this).css({'height':
                    $(this).prev().outerHeight()});
            },
            '_update': function( e, data ) {
                $(this)
                    .contents()
                    .find('body')
                    .html(data.html);
            }
        })
        .trigger('_resize')
        .appendTo( $codemirror );

    /* update iframe contents for the first time */
    updatePreview( $codemirror.get(0).CodeMirror );
}



/* end jQuery closure and document ready */
}); })(markupmirror.jQuery);
