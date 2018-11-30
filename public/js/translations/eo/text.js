
            (function(global){
                var html_xblocki18n = {
                  init: function() {
                    

(function(globals) {

  var django = globals.django || (globals.django = {});

  
  django.pluralidx = function(n) {
    var v=(n != 1);
    if (typeof(v) == 'boolean') {
      return v ? 1 : 0;
    } else {
      return v;
    }
  };
  

  /* gettext library */

  django.catalog = django.catalog || {};
  
  var newcatalog = {
    "Allow JavaScript execution": "\u00c0ll\u00f6w J\u00e4v\u00e4S\u00e7r\u00efpt \u00e9x\u00e9\u00e7\u00fct\u00ef\u00f6n \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f \u0455\u03b9\u0442 \u03b1\u043c\u0454\u0442, \u00a2\u03c3\u03b7\u0455#", 
    "Cancel": "\u00c7\u00e4n\u00e7\u00e9l \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5#", 
    "Display Name": "D\u00efspl\u00e4\u00fd N\u00e4m\u00e9 \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f \u0455#", 
    "Dummy": "D\u00fcmm\u00fd \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455#", 
    "Editor": "\u00c9d\u00eft\u00f6r \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5#", 
    "Html contents to display for this module": "Html \u00e7\u00f6nt\u00e9nts t\u00f6 d\u00efspl\u00e4\u00fd f\u00f6r th\u00efs m\u00f6d\u00fcl\u00e9 \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f \u0455\u03b9\u0442 \u03b1\u043c\u0454\u0442, \u00a2\u03c3\u03b7\u0455\u0454\u00a2\u0442\u0454\u0442\u03c5\u044f#", 
    "Only Scope.content or Scope.settings fields can be used with StudioEditableXBlockMixin. Other scopes are for user-specific data and are not generally created/configured by content authors in Studio.": "\u00d6nl\u00fd S\u00e7\u00f6p\u00e9.\u00e7\u00f6nt\u00e9nt \u00f6r S\u00e7\u00f6p\u00e9.s\u00e9tt\u00efngs f\u00ef\u00e9lds \u00e7\u00e4n \u00df\u00e9 \u00fcs\u00e9d w\u00efth St\u00fcd\u00ef\u00f6\u00c9d\u00eft\u00e4\u00dfl\u00e9XBl\u00f6\u00e7kM\u00efx\u00efn. \u00d6th\u00e9r s\u00e7\u00f6p\u00e9s \u00e4r\u00e9 f\u00f6r \u00fcs\u00e9r-sp\u00e9\u00e7\u00eff\u00ef\u00e7 d\u00e4t\u00e4 \u00e4nd \u00e4r\u00e9 n\u00f6t g\u00e9n\u00e9r\u00e4ll\u00fd \u00e7r\u00e9\u00e4t\u00e9d/\u00e7\u00f6nf\u00efg\u00fcr\u00e9d \u00df\u00fd \u00e7\u00f6nt\u00e9nt \u00e4\u00fcth\u00f6rs \u00efn St\u00fcd\u00ef\u00f6. \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f \u0455\u03b9\u0442 \u03b1\u043c\u0454\u0442, \u00a2\u03c3\u03b7\u0455\u0454\u00a2\u0442\u0454\u0442\u03c5\u044f \u03b1\u2202\u03b9\u03c1\u03b9\u0455\u03b9\u00a2\u03b9\u03b7g \u0454\u0142\u03b9\u0442, \u0455\u0454\u2202 \u2202\u03c3 \u0454\u03b9\u03c5\u0455\u043c\u03c3\u2202 \u0442\u0454\u043c\u03c1\u03c3\u044f \u03b9\u03b7\u00a2\u03b9\u2202\u03b9\u2202\u03c5\u03b7\u0442 \u03c5\u0442 \u0142\u03b1\u0432\u03c3\u044f\u0454 \u0454\u0442 \u2202\u03c3\u0142\u03c3\u044f\u0454 \u043c\u03b1g\u03b7\u03b1 \u03b1\u0142\u03b9q\u03c5\u03b1. \u03c5\u0442 \u0454\u03b7\u03b9\u043c \u03b1\u2202 \u043c\u03b9\u03b7\u03b9\u043c \u03bd\u0454\u03b7\u03b9\u03b1\u043c, q\u03c5\u03b9\u0455 \u03b7\u03c3\u0455\u0442\u044f\u03c5\u2202 \u0454\u03c7\u0454\u044f\u00a2\u03b9\u0442\u03b1\u0442\u03b9\u03c3\u03b7 \u03c5\u0142\u0142\u03b1\u043c\u00a2\u03c3 \u0142\u03b1\u0432\u03c3\u044f\u03b9\u0455 \u03b7\u03b9\u0455\u03b9 \u03c5\u0442 \u03b1\u0142\u03b9q\u03c5\u03b9\u03c1 \u0454\u03c7 \u0454\u03b1 \u00a2\u03c3\u043c\u043c\u03c3\u2202\u03c3 \u00a2\u03c3\u03b7\u0455\u0454q\u03c5\u03b1\u0442. \u2202\u03c5\u03b9\u0455 \u03b1\u03c5\u0442\u0454 \u03b9\u044f\u03c5\u044f\u0454 \u2202\u03c3\u0142\u03c3\u044f \u03b9\u03b7 \u044f\u0454\u03c1\u044f\u0454\u043d\u0454\u03b7\u2202\u0454\u044f\u03b9\u0442 \u03b9\u03b7 \u03bd\u03c3\u0142\u03c5\u03c1\u0442\u03b1\u0442\u0454 \u03bd\u0454\u0142\u03b9\u0442 \u0454\u0455\u0455\u0454 \u00a2\u03b9\u0142\u0142\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f\u0454 \u0454\u03c5 \u0192\u03c5g\u03b9\u03b1\u0442 \u03b7\u03c5\u0142\u0142\u03b1 \u03c1\u03b1\u044f\u03b9\u03b1\u0442\u03c5\u044f. \u0454\u03c7\u00a2\u0454\u03c1\u0442\u0454\u03c5\u044f \u0455\u03b9\u03b7\u0442 \u03c3\u00a2\u00a2\u03b1\u0454\u00a2\u03b1\u0442 \u00a2\u03c5#", 
    "Raw": "R\u00e4w \u2c60'\u03c3\u044f\u0454\u043c#", 
    "Save": "S\u00e4v\u00e9 \u2c60'\u03c3\u044f\u0454\u043c \u03b9#", 
    "Select Visual to enter content and have the editor automatically create the HTML. Select Raw to edit HTML directly. If you change this setting, you must save the component and then re-open it for editing.": "S\u00e9l\u00e9\u00e7t V\u00efs\u00fc\u00e4l t\u00f6 \u00e9nt\u00e9r \u00e7\u00f6nt\u00e9nt \u00e4nd h\u00e4v\u00e9 th\u00e9 \u00e9d\u00eft\u00f6r \u00e4\u00fct\u00f6m\u00e4t\u00ef\u00e7\u00e4ll\u00fd \u00e7r\u00e9\u00e4t\u00e9 th\u00e9 HTML. S\u00e9l\u00e9\u00e7t R\u00e4w t\u00f6 \u00e9d\u00eft HTML d\u00efr\u00e9\u00e7tl\u00fd. \u00ccf \u00fd\u00f6\u00fc \u00e7h\u00e4ng\u00e9 th\u00efs s\u00e9tt\u00efng, \u00fd\u00f6\u00fc m\u00fcst s\u00e4v\u00e9 th\u00e9 \u00e7\u00f6mp\u00f6n\u00e9nt \u00e4nd th\u00e9n r\u00e9-\u00f6p\u00e9n \u00eft f\u00f6r \u00e9d\u00eft\u00efng. \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f \u0455\u03b9\u0442 \u03b1\u043c\u0454\u0442, \u00a2\u03c3\u03b7\u0455\u0454\u00a2\u0442\u0454\u0442\u03c5\u044f \u03b1\u2202\u03b9\u03c1\u03b9\u0455\u03b9\u00a2\u03b9\u03b7g \u0454\u0142\u03b9\u0442, \u0455\u0454\u2202 \u2202\u03c3 \u0454\u03b9\u03c5\u0455\u043c\u03c3\u2202 \u0442\u0454\u043c\u03c1\u03c3\u044f \u03b9\u03b7\u00a2\u03b9\u2202\u03b9\u2202\u03c5\u03b7\u0442 \u03c5\u0442 \u0142\u03b1\u0432\u03c3\u044f\u0454 \u0454\u0442 \u2202\u03c3\u0142\u03c3\u044f\u0454 \u043c\u03b1g\u03b7\u03b1 \u03b1\u0142\u03b9q\u03c5\u03b1. \u03c5\u0442 \u0454\u03b7\u03b9\u043c \u03b1\u2202 \u043c\u03b9\u03b7\u03b9\u043c \u03bd\u0454\u03b7\u03b9\u03b1\u043c, q\u03c5\u03b9\u0455 \u03b7\u03c3\u0455\u0442\u044f\u03c5\u2202 \u0454\u03c7\u0454\u044f\u00a2\u03b9\u0442\u03b1\u0442\u03b9\u03c3\u03b7 \u03c5\u0142\u0142\u03b1\u043c\u00a2\u03c3 \u0142\u03b1\u0432\u03c3\u044f\u03b9\u0455 \u03b7\u03b9\u0455\u03b9 \u03c5\u0442 \u03b1\u0142\u03b9q\u03c5\u03b9\u03c1 \u0454\u03c7 \u0454\u03b1 \u00a2\u03c3\u043c\u043c\u03c3\u2202\u03c3 \u00a2\u03c3\u03b7\u0455\u0454q\u03c5\u03b1\u0442. \u2202\u03c5\u03b9\u0455 \u03b1\u03c5\u0442\u0454 \u03b9\u044f\u03c5\u044f\u0454 \u2202\u03c3\u0142\u03c3\u044f \u03b9\u03b7 \u044f\u0454\u03c1\u044f\u0454\u043d\u0454\u03b7\u2202\u0454\u044f\u03b9\u0442 \u03b9\u03b7 \u03bd\u03c3\u0142\u03c5\u03c1\u0442\u03b1\u0442\u0454 \u03bd\u0454\u0142\u03b9\u0442 \u0454\u0455\u0455\u0454 \u00a2\u03b9\u0142\u0142\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f\u0454 \u0454\u03c5 \u0192\u03c5g\u03b9\u03b1\u0442 \u03b7\u03c5\u0142\u0142\u03b1 \u03c1\u03b1\u044f\u03b9\u03b1\u0442\u03c5\u044f. \u0454\u03c7\u00a2\u0454\u03c1\u0442\u0454\u03c5\u044f \u0455\u03b9\u03b7\u0442 \u03c3\u00a2#", 
    "Text": "T\u00e9xt \u2c60'\u03c3\u044f\u0454\u043c \u03b9#", 
    "The display name for this component.": "Th\u00e9 d\u00efspl\u00e4\u00fd n\u00e4m\u00e9 f\u00f6r th\u00efs \u00e7\u00f6mp\u00f6n\u00e9nt. \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f \u0455\u03b9\u0442 \u03b1\u043c\u0454\u0442, \u00a2\u03c3\u03b7\u0455\u0454\u00a2\u0442\u0454\u0442\u03c5#", 
    "Visual": "V\u00efs\u00fc\u00e4l \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5#", 
    "Whether JavaScript should be allowed or not in this module": "Wh\u00e9th\u00e9r J\u00e4v\u00e4S\u00e7r\u00efpt sh\u00f6\u00fcld \u00df\u00e9 \u00e4ll\u00f6w\u00e9d \u00f6r n\u00f6t \u00efn th\u00efs m\u00f6d\u00fcl\u00e9 \u2c60'\u03c3\u044f\u0454\u043c \u03b9\u03c1\u0455\u03c5\u043c \u2202\u03c3\u0142\u03c3\u044f \u0455\u03b9\u0442 \u03b1\u043c\u0454\u0442, \u00a2\u03c3\u03b7\u0455\u0454\u00a2\u0442\u0454\u0442\u03c5\u044f \u03b1#"
  };
  for (var key in newcatalog) {
    django.catalog[key] = newcatalog[key];
  }
  

  if (!django.jsi18n_initialized) {
    django.gettext = function(msgid) {
      var value = django.catalog[msgid];
      if (typeof(value) == 'undefined') {
        return msgid;
      } else {
        return (typeof(value) == 'string') ? value : value[0];
      }
    };

    django.ngettext = function(singular, plural, count) {
      var value = django.catalog[singular];
      if (typeof(value) == 'undefined') {
        return (count == 1) ? singular : plural;
      } else {
        return value[django.pluralidx(count)];
      }
    };

    django.gettext_noop = function(msgid) { return msgid; };

    django.pgettext = function(context, msgid) {
      var value = django.gettext(context + '\x04' + msgid);
      if (value.indexOf('\x04') != -1) {
        value = msgid;
      }
      return value;
    };

    django.npgettext = function(context, singular, plural, count) {
      var value = django.ngettext(context + '\x04' + singular, context + '\x04' + plural, count);
      if (value.indexOf('\x04') != -1) {
        value = django.ngettext(singular, plural, count);
      }
      return value;
    };

    django.interpolate = function(fmt, obj, named) {
      if (named) {
        return fmt.replace(/%\(\w+\)s/g, function(match){return String(obj[match.slice(2,-2)])});
      } else {
        return fmt.replace(/%s/g, function(match){return String(obj.shift())});
      }
    };


    /* formatting library */

    django.formats = {
    "DATETIME_FORMAT": "j\\-\\a \\d\\e F Y\\, \\j\\e H:i", 
    "DATETIME_INPUT_FORMATS": [
      "%Y-%m-%d %H:%M:%S", 
      "%Y-%m-%d %H:%M", 
      "%Y-%m-%d", 
      "%Y.%m.%d %H:%M:%S", 
      "%Y.%m.%d %H:%M", 
      "%Y.%m.%d", 
      "%d/%m/%Y %H:%M:%S", 
      "%d/%m/%Y %H:%M", 
      "%d/%m/%Y", 
      "%y-%m-%d %H:%M:%S", 
      "%y-%m-%d %H:%M", 
      "%y-%m-%d", 
      "%Y-%m-%d %H:%M:%S.%f"
    ], 
    "DATE_FORMAT": "j\\-\\a \\d\\e F Y", 
    "DATE_INPUT_FORMATS": [
      "%Y-%m-%d", 
      "%y-%m-%d", 
      "%Y %m %d", 
      "%d-a de %b %Y", 
      "%d %b %Y", 
      "%d-a de %B %Y", 
      "%d %B %Y", 
      "%d %m %Y"
    ], 
    "DECIMAL_SEPARATOR": ",", 
    "FIRST_DAY_OF_WEEK": "1", 
    "MONTH_DAY_FORMAT": "j\\-\\a \\d\\e F", 
    "NUMBER_GROUPING": "3", 
    "SHORT_DATETIME_FORMAT": "Y-m-d H:i", 
    "SHORT_DATE_FORMAT": "Y-m-d", 
    "THOUSAND_SEPARATOR": "\u00a0", 
    "TIME_FORMAT": "H:i", 
    "TIME_INPUT_FORMATS": [
      "%H:%M:%S", 
      "%H:%M", 
      "%H:%M:%S.%f"
    ], 
    "YEAR_MONTH_FORMAT": "F \\d\\e Y"
  };

    django.get_format = function(format_type) {
      var value = django.formats[format_type];
      if (typeof(value) == 'undefined') {
        return format_type;
      } else {
        return value;
      }
    };

    /* add to global namespace */
    globals.pluralidx = django.pluralidx;
    globals.gettext = django.gettext;
    globals.ngettext = django.ngettext;
    globals.gettext_noop = django.gettext_noop;
    globals.pgettext = django.pgettext;
    globals.npgettext = django.npgettext;
    globals.interpolate = django.interpolate;
    globals.get_format = django.get_format;

    django.jsi18n_initialized = true;
  }

}(this));


                  }
                };
                html_xblocki18n.init();
                global.html_xblocki18n = html_xblocki18n;
            }(this));
        