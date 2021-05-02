function removeRow(e){
	e.preventDefault();
	$(e.target).parent().parent().parent().remove();
}


$(document).ready(function () {
	var newAcademicsNo = 1 ;
	$('.add-more').on('click touchstart',  function (e) {
		e.preventDefault();
		var newIn ='<tr class="appliRow'+newAcademicsNo+'" id="field1"> <td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="othCourse' + newAcademicsNo +'" id="othCourse' + newAcademicsNo +'" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Enter Course" required></td><td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="othName' + newAcademicsNo +'" id="othName' + newAcademicsNo +'" style="margin: 0; background-color: transparent; border:none;" placeholder="Name of Board/College/University"  required></td><td class="col-1" style="text-align: center; padding: 0;">'+
		'<input type="text" name="othPercent' + newAcademicsNo +'" id="othPercent' + newAcademicsNo +'" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="% of Marks" required></td><td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="othSubject' + newAcademicsNo +'" id="othSubject' + newAcademicsNo +'" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Subject(s)" required></td><td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;">'+
		'<select name="yearOfPassing'+ parseInt(newAcademicsNo+5) +'" id="yearOfPassing'+ parseInt(newAcademicsNo+5) +'" ></select></td><td class="col-3" style="display:flex;place-content:space-between">'+
		'<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="othFile' + newAcademicsNo +'" name="othFile' + newAcademicsNo +'"></span>'+
		'<span style="display:inline"><button onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>'+
		'</td></tr>' ;
	$('.academic-tbody').append(newIn);

  // console.log("hvgvcvdgcvdvcgdvc");
  var yearId ='yearOfPassing'+ parseInt(newAcademicsNo+5);
  var ele = document.getElementById(yearId);
  console.log(ele);
  var presYear = new Date();
  for (let i = presYear.getFullYear(); i >= 1950; i--) {
    // console.log(i);
    var op= document.createElement('option');
    op.value = i;
    op.textContent = i;
    ele.appendChild(op);
    // ele.innerHTML += '<option value=' + i + '>' + i + '</option>\n'
  }
	newAcademicsNo+=1;
  });

});

(function ($) {
  var $window = $(window),
    $body = $('body'),
    $main = $('#main');

  // Breakpoints.
  breakpoints({
    xlarge: ['1281px', '1680px'],
    large: ['981px', '1280px'],
    medium: ['737px', '980px'],
    small: ['481px', '736px'],
    xsmall: ['361px', '480px'],
    xxsmall: [null, '360px'],
  });

  // Play initial animations on page load.
  $window.on('load', function () {
    window.setTimeout(function () {
      $body.removeClass('is-preload');
    }, 100);
  });

  // Nav.
  var $nav = $('#nav');

  if ($nav.length > 0) {
    // Shrink effect.
    $main.scrollex({
      mode: 'top',
      enter: function () {
        $nav.addClass('alt');
      },
      leave: function () {
        $nav.removeClass('alt');
      },
    });

    // Links.
    var $nav_a = $nav.find('a');

    $nav_a
      .scrolly({
        speed: 1000,
        offset: function () {
          return $nav.height();
        },
      })
      .on('click', function () {
        var $this = $(this);

        // External link? Bail.
        if ($this.attr('href').charAt(0) != '#') return;

        // Deactivate all links.
        $nav_a.removeClass('active').removeClass('active-locked');

        // Activate link *and* lock it (so Scrollex doesn't try to activate other links as we're scrolling to this one's section).
        $this.addClass('active').addClass('active-locked');
      })
      .each(function () {
        var $this = $(this),
          id = $this.attr('href'),
          $section = $(id);

        // No section for this link? Bail.
        if ($section.length < 1) return;

        // Scrollex.
        $section.scrollex({
          mode: 'middle',
          initialize: function () {
            // Deactivate section.
            if (browser.canUse('transition')) $section.addClass('inactive');
          },
          enter: function () {
            // Activate section.
            $section.removeClass('inactive');

            // No locked links? Deactivate all links and activate this section's one.
            if ($nav_a.filter('.active-locked').length == 0) {
              $nav_a.removeClass('active');
              $this.addClass('active');
            }

            // Otherwise, if this section's link is the one that's locked, unlock it.
            else if ($this.hasClass('active-locked'))
              $this.removeClass('active-locked');
          },
        });
      });
  }

  // Scrolly.
  $('.scrolly').scrolly({
    speed: 1000,
  });
})(jQuery);

/////   Profile Pic   /////
$('#profileImage').click(function (e) {
  $('#imageUpload').click();
});
function fasterPreview(uploader) {
  if (uploader.files && uploader.files[0]) {
    $('#profileImage').attr(
      'src',
      window.URL.createObjectURL(uploader.files[0])
    );
  }
}

$('#imageUpload').change(function () {
  fasterPreview(this);
});



////   Upload Signatures   //////
$('#signImage').click(function (e) {
  $('#signUpload').click();
});
function fasterPreview2(uploader) {
  if (uploader.files && uploader.files[0]) {
    $('#signImage').attr(
      'src',
      window.URL.createObjectURL(uploader.files[0])
    );
  }
}

$('#signUpload').change(function () {
  fasterPreview2(this);
});

