$(function () {
  // $.resize(function() {
    $("canvas.square-backgrounds")[0].width = 1000;
    $("canvas.square-backgrounds")[0].height = 1000;
    $.redrawCanvas();
    var image = $("canvas.square-backgrounds")[0].toDataURL();
    $(".jumbotron").css("background", "transparent url('"+image+"') repeat");
  // })

  $('pre').each(function(i,block) {
    hljs.highlightBlock(block);
  });

  $('div.spoilers pre').each(function(i,block) {
    hljs.highlightBlock(block);
  });

  $("textarea").keydown(function(e) {
    if(e.keyCode === 9) { // tab was pressed
      console.log("Tab was pressed");
      // get caret position/selection
      var start = this.selectionStart;
      var end = this.selectionEnd;

      var $this = $(this);
      var value = $this.val();

      // set textarea value to: text before caret + tab + text after caret
      $this.val(value.substring(0, start)
                  + "\t"
                  + value.substring(end));

      // put caret at right position again (add one for the tab)
      this.selectionStart = this.selectionEnd = start + 1;

      // prevent the focus lose
      e.preventDefault();
    }
  });

  function checkPlatform(mac,win32,win64,linux,other) {
    if (navigator.platform == "MacIntel") {   // MAC
      mac();
    } else if (navigator.userAgent.indexOf('WOW64')>-1 || 
               window.navigator.platform=='Win64') {  // WIN64
      win64();
    } else if (navigator.platform == "Win32") {      // WIN32
      win32();
    } else if (navigator.platform.startsWith("Linux")) {
      linux();
    } else {
      other();
    }
  }

  $('.win32').hide();
  $('.win64').hide();
  $('.linux').hide();
  $('.win').hide();
  $('.mac').hide();
  

  checkPlatform(
    function mac() {
      console.log("mac")
      $('.mac').show();
      $('#download-haskell').attr("href", 
        "https://www.haskell.org/platform/download/2014.2.0.0/Haskell%20Platform%202014.2.0.0%2064bit.signed.pkg")
      $('#exe-name').html( 
        "Haskell Platform 2014.2.0.0 64bit.signed.pkg")
    
    },
    function win32() {
      console.log("win32")
      $('.win').show();
      $('#download-haskell').attr("href", 
        "https://www.haskell.org/platform/download/2014.2.0.0/HaskellPlatform-2014.2.0.0-x86_64-setup.exe")
      $('#exe-name').html( 
        "HaskellPlatform-2014.2.0.0-x86_64-setup.exe")
    },
    function win64() {
      console.log("win64")
      $('.win').show();
      $('#download-haskell').attr("href", 
        "https://www.haskell.org/platform/download/2014.2.0.0/HaskellPlatform-2014.2.0.0-i386-setup.exe")
      $('#exe-name').html(
        "HaskellPlatform-2014.2.0.0-i386-setup.exe")
    },
    function linux() {      
      console.log("linux")
      $('.linux').show();
      $('#download-haskell').attr("href", 
        "https://www.haskell.org/platform/linux.html#binary")
      $('#exe-name').html(
        "linux.html#binary")
    },
    function other() {
      console.log("other")
      $('#download-haskell').attr("href", 
        "https://www.haskell.org/platform/")
      $('#exe-name').html( 
        "Haskell")
    })
  $(document).delegate('textbox', 'keydown', function(e) { 
    var keyCode = e.keyCode || e.which; 

    if (keyCode == 9) { 
      e.preventDefault(); 
      var start = $(this).get(0).selectionStart;
      var end = $(this).get(0).selectionEnd;

      // set textarea value to: text before caret + tab + text after caret
      $(this).val($(this).val().substring(0, start)
                  + "\t"
                  + $(this).val().substring(end));

      // put caret at right position again
      $(this).get(0).selectionStart = 
      $(this).get(0).selectionEnd = start + 1;
    } 
  });



})
    