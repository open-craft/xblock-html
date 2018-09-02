/* Javascript for HTMLXBlock. */
var CUSTOM_FONTS, STANDARD_FONTS, _getFonts;

CUSTOM_FONTS = "Default='Open Sans', Verdana, Arial, Helvetica, sans-serif;";
STANDARD_FONTS = "Andale Mono=andale mono,times;" + "Arial=arial,helvetica,sans-serif;" + "Arial Black=arial black,avant garde;" + "Book Antiqua=book antiqua,palatino;" + "Comic Sans MS=comic sans ms,sans-serif;" + "Courier New=courier new,courier;" + "Georgia=georgia,palatino;" + "Helvetica=helvetica;" + "Impact=impact,chicago;" + "Symbol=symbol;" + "Tahoma=tahoma,arial,helvetica,sans-serif;" + "Terminal=terminal,monaco;" + "Times New Roman=times new roman,times;" + "Trebuchet MS=trebuchet ms,geneva;" + "Verdana=verdana,geneva;" + "Webdings=webdings;" + "Wingdings=wingdings,zapf dingbats";

_getFonts = function () {
  return CUSTOM_FONTS + STANDARD_FONTS;
};

var PLUGINS, PLUGINS_DIR, _getExternalPlugins;

PLUGINS = ["codesample", "image", "link", "lists", "textcolor", "codemirror"];
PLUGINS_DIR = "/resource/html5/public/plugins/";

_getExternalPlugins = function () {
  var externalPlugins = {};

  for (let plugin of PLUGINS) {
    externalPlugins[plugin] = PLUGINS_DIR + plugin + "/plugin.min.js"
  }
  return externalPlugins
};

function HTML5XBlock(runtime, element) {
  var editorChoice = $("#editor-tab").data("editor");
  var contentSelector = "textarea#html5-textarea";
  var editor;

  $(function ($) {
    if (editorChoice === "visual") {
      editor = tinymce.init({
        skin_url: "/resource/html5/public/skin",
        theme: "modern",
        schema: "html5",
        convert_urls: false,
        directionality: $(".wrapper-view, .window-wrap").prop('dir'),
        selector: contentSelector,
        menubar: false,
        statusbar: false,
        valid_elements: "*[*]",
        extended_valid_elements: "*[*]",
        valid_children: "+body[style]",
        invalid_elements: "",
        font_formats: _getFonts(),
        toolbar: "formatselect | fontselect | bold italic underline forecolor codesample | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent blockquote | link unlink image | code",
        external_plugins: _getExternalPlugins(),
        formats: {
          code: {
            inline: 'code'
          }
        },
        visual: false,
        image_advtab: true,
        block_formats: "Paragraph=p;Preformatted=pre;Heading 3=h3;Heading 4=h4;Heading 5=h5;Heading 6=h6",
        width: '100%',
        height: '400px',
        browser_spellcheck: true,
        codemirror: {
          fullscreen: true,
          width: 800,
          height: 600,
          saveCursorPosition: true,
          config: {
            mode: 'text/html',
          }
        }
      });
    } else {
      editor = CodeMirror.fromTextArea($(contentSelector, this.element)[0], {
        mode: "text/html",
        lineNumbers: true,
        matchBrackets: true,
        lineWrapping: true
      });
    }
  });

  $(".save-button", element).click(function (eventObject) {
    var handlerUrl = runtime.handlerUrl(element, "update_content");
    var content = (editorChoice === "visual") ? tinymce.get("html5-textarea").getContent() : editor.getValue();

    $.ajax({
      type: "POST",
      url: handlerUrl,
      data: JSON.stringify({"content": content})
    });
  });
}
