/* Javascript for HTMLXBlock. */

const CUSTOM_FONTS = "Default='Open Sans', Verdana, Arial, Helvetica, sans-serif;";
const STANDARD_FONTS = "Andale Mono=andale mono,times;" + "Arial=arial,helvetica,sans-serif;" + "Arial Black=arial black,avant garde;" + "Book Antiqua=book antiqua,palatino;" + "Comic Sans MS=comic sans ms,sans-serif;" + "Courier New=courier new,courier;" + "Georgia=georgia,palatino;" + "Helvetica=helvetica;" + "Impact=impact,chicago;" + "Symbol=symbol;" + "Tahoma=tahoma,arial,helvetica,sans-serif;" + "Terminal=terminal,monaco;" + "Times New Roman=times new roman,times;" + "Trebuchet MS=trebuchet ms,geneva;" + "Verdana=verdana,geneva;" + "Webdings=webdings;" + "Wingdings=wingdings,zapf dingbats";
const FONTS = CUSTOM_FONTS + STANDARD_FONTS;

const PLUGINS = ["codesample", "image", "link", "lists", "textcolor", "codemirror"];
const PLUGINS_DIR = "/resource/html5/public/plugins/";
const EXTERNAL_PLUGINS = PLUGINS.map(function(p) { return PLUGINS_DIR + p + "/plugin.min.js" });

function HTML5XBlock(runtime, element) {
  const editorTab = document.getElementById("editor-tab");
  const contentSelector = "textarea#html5-textarea";
  var editor;

  window.addEventListener('load', function () {
    const languageWrapper = document.querySelectorAll(".wrapper-view, .window-wrap");
    const directionality = (languageWrapper.length > 0) ? languageWrapper.dir : "ltr";

    if (editorTab.dataset.editor === "visual") {
      editor = tinymce.init({
        skin_url: "/resource/html5/public/skin",
        theme: "modern",
        schema: "html5",
        convert_urls: false,
        directionality: directionality,
        selector: contentSelector,
        menubar: false,
        statusbar: false,
        valid_elements: "*[*]",
        extended_valid_elements: "*[*]",
        valid_children: "+body[style]",
        invalid_elements: "",
        font_formats: FONTS,
        toolbar: "formatselect | fontselect | bold italic underline forecolor codesample | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent blockquote | link unlink image | code",
        external_plugins: EXTERNAL_PLUGINS,
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
      editor = CodeMirror.fromTextArea(document.querySelectorAll(contentSelector)[0], {
        mode: "text/html",
        lineNumbers: true,
        matchBrackets: true,
        lineWrapping: true
      });
    }
  }, false);

  document.getElementById("save-button").addEventListener("click", function () {
    const handlerUrl = runtime.handlerUrl(element, "update_content");
    const content = (editorTab.dataset.editor === "visual") ? tinymce.get("html5-textarea").getContent() : editor.getValue();

    $.ajax({
      type: "POST",
      url: handlerUrl,
      data: JSON.stringify({"content": content})
    });
  });
}
