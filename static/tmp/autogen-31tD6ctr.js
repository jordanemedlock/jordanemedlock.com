function hident2(){if(navigator.id){navigator.id.watch({onlogin:function(assertion){if(assertion)document.location="/auth/page/browserid/"+assertion},onlogout:function(){}});navigator.id.request({returnTo:"/auth/login"+"?autologin=true"})}else alert("Loading, please try again")};(function(){var bid=document.createElement("script");bid.async=true;bid.src="https://login.persona.org/include.js";var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(bid,s)})();$(function(){$("textarea").keydown(function(e){if(e.keyCode===9){console.log("Tab was pressed");var start=this.selectionStart,end=this.selectionEnd,$this=$(this),value=$this.val();$this.val(value.substring(0,start)+"\t"+value.substring(end));this.selectionStart=this.selectionEnd=start+1;e.preventDefault()}})
function checkPlatform(mac,win32,win64,linux,other){if(navigator.platform=="MacIntel"){mac()}else if(navigator.userAgent.indexOf('WOW64')>-1||window.navigator.platform=='Win64'){win64()}else if(navigator.platform=="Win32"){win32()}else if(navigator.platform.startsWith("Linux")){linux()}else other()};$('.win32').hide();$('.win64').hide();$('.linux').hide();$('.win').hide();$('.mac').hide();checkPlatform(function mac(){console.log("mac");$('.mac').show();$('#download-haskell').attr("href","https://www.haskell.org/platform/download/2014.2.0.0/Haskell%20Platform%202014.2.0.0%2064bit.signed.pkg");$('#exe-name').html("Haskell Platform 2014.2.0.0 64bit.signed.pkg")},function win32(){console.log("win32");$('.win').show();$('#download-haskell').attr("href","https://www.haskell.org/platform/download/2014.2.0.0/HaskellPlatform-2014.2.0.0-x86_64-setup.exe");$('#exe-name').html("HaskellPlatform-2014.2.0.0-x86_64-setup.exe")},function win64(){console.log("win64");$('.win').show();$('#download-haskell').attr("href","https://www.haskell.org/platform/download/2014.2.0.0/HaskellPlatform-2014.2.0.0-i386-setup.exe");$('#exe-name').html("HaskellPlatform-2014.2.0.0-i386-setup.exe")},function linux(){console.log("linux");$('.linux').show();$('#download-haskell').attr("href","https://www.haskell.org/platform/linux.html#binary");$('#exe-name').html("linux.html#binary")},function other(){console.log("other");$('#download-haskell').attr("href","https://www.haskell.org/platform/");$('#exe-name').html("Haskell")});$(document).delegate('textbox','keydown',function(e){var keyCode=e.keyCode||e.which;if(keyCode==9){e.preventDefault();var start=$(this).get(0).selectionStart,end=$(this).get(0).selectionEnd;$(this).val($(this).val().substring(0,start)+"\t"+$(this).val().substring(end));$(this).get(0).selectionStart=$(this).get(0).selectionEnd=start+1}})})