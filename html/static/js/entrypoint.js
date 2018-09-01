/* Javascript for HTMLXBlock. */
function HTML5XBlock(runtime, element) {
  $(function ($) {
    var contentSelector = "textarea#html5-textarea";
    var pluginsDir = "/resource/html5/public/plugins/";
    var plugins = ["code", "codesample", "image", "link", "lists", "textcolor"];
    var externalPlugins = {};

    for (let plugin of plugins) {
      externalPlugins[plugin] = pluginsDir + plugin + "/plugin.min.js"
    }

    tinymce.init({
      skin_url: "/resource/html5/public/skin",
      selector: contentSelector,
      menubar: false,
      statusbar: false,
      toolbar: "formatselect | fontselect | bold italic underline forecolor codesample | bullist numlist outdent indent blockquote | link unlink image | code",
      external_plugins: externalPlugins
    });
  });

  var handlerUrl = runtime.handlerUrl(element, "update_content");
  $(".save-button", element).click(function (eventObject) {
    tinyMCE.triggerSave();
    $.ajax({
      type: "POST",
      url: handlerUrl,
      data: JSON.stringify({"content": tinymce.get("html5-textarea").getContent()})
    });
  });
}
