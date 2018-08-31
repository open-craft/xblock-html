tinymce.init({
  skin_url: "/resource/html5/public/skin",
  selector: "textarea",
  menubar:false,
  statusbar: false,
  toolbar: "formatselect | fontselect | bold italic underline forecolor codesample | bullist numlist outdent indent blockquote | link unlink image | code",
  external_plugins: {
    'code': '/resource/html5/public/plugins/code/plugin.min.js',
    'codesample': '/resource/html5/public/plugins/codesample/plugin.min.js',
    'image': '/resource/html5/public/plugins/image/plugin.min.js',
    'link': '/resource/html5/public/plugins/link/plugin.min.js',
    'lists': '/resource/html5/public/plugins/lists/plugin.min.js',
    'textcolor': '/resource/html5/public/plugins/textcolor/plugin.min.js'
  }
});
