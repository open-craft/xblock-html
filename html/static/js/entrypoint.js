tinymce.init({
  skin_url: "/resource/html/public/skin",
  selector: "textarea",
  menubar:false,
  statusbar: false,
  toolbar: "formatselect | fontselect | bold italic underline forecolor codesample | bullist numlist outdent indent blockquote | link unlink image | code",
  external_plugins: {
    'code': '/resource/html/public/plugins/code/plugin.min.js',
    'codesample': '/resource/html/public/plugins/codesample/plugin.min.js',
    'image': '/resource/html/public/plugins/image/plugin.min.js',
    'link': '/resource/html/public/plugins/link/plugin.min.js',
    'lists': '/resource/html/public/plugins/lists/plugin.min.js',
    'textcolor': '/resource/html/public/plugins/textcolor/plugin.min.js'
  }
});
