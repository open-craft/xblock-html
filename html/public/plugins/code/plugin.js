(function () {
var code = (function () {
  'use strict';

  var global = tinymce.util.Tools.resolve('tinymce.PluginManager');

  var global$1 = tinymce.util.Tools.resolve('tinymce.dom.DOMUtils');

  var getMinWidth = function (editor) {
    return editor.getParam('code_dialog_width', 600);
  };
  var getMinHeight = function (editor) {
    return editor.getParam('code_dialog_height', Math.min(global$1.DOM.getViewPort().h - 200, 500));
  };
  var $_cu85j9a2jlhp4ft3 = {
    getMinWidth: getMinWidth,
    getMinHeight: getMinHeight
  };

  var setContent = function (editor, html) {
    editor.focus();
    editor.undoManager.transact(function () {
      editor.setContent(html);
    });
    editor.selection.setCursorLocation();
    editor.nodeChanged();
  };
  var getContent = function (editor) {
    return editor.getContent({ source_view: true });
  };
  var $_5x3lvba4jlhp4ft7 = {
    setContent: setContent,
    getContent: getContent
  };

  var open = function (editor) {
    var minWidth = $_cu85j9a2jlhp4ft3.getMinWidth(editor);
    var minHeight = $_cu85j9a2jlhp4ft3.getMinHeight(editor);
    var win = editor.windowManager.open({
      title: 'Source code',
      body: {
        type: 'textbox',
        name: 'code',
        multiline: true,
        minWidth: minWidth,
        minHeight: minHeight,
        spellcheck: false,
        style: 'direction: ltr; text-align: left'
      },
      onSubmit: function (e) {
        $_5x3lvba4jlhp4ft7.setContent(editor, e.data.code);
      }
    });
    win.find('#code').value($_5x3lvba4jlhp4ft7.getContent(editor));
  };
  var $_b1h62ba1jlhp4ft1 = { open: open };

  var register = function (editor) {
    editor.addCommand('mceCodeEditor', function () {
      $_b1h62ba1jlhp4ft1.open(editor);
    });
  };
  var $_4tcj7pa0jlhp4fsz = { register: register };

  var register$1 = function (editor) {
    editor.addButton('code', {
      icon: 'code',
      tooltip: 'Source code',
      onclick: function () {
        $_b1h62ba1jlhp4ft1.open(editor);
      }
    });
    editor.addMenuItem('code', {
      icon: 'code',
      text: 'Source code',
      onclick: function () {
        $_b1h62ba1jlhp4ft1.open(editor);
      }
    });
  };
  var $_9cyztsa5jlhp4fta = { register: register$1 };

  global.add('code', function (editor) {
    $_4tcj7pa0jlhp4fsz.register(editor);
    $_9cyztsa5jlhp4fta.register(editor);
    return {};
  });
  function Plugin () {
  }

  return Plugin;

}());
})();
