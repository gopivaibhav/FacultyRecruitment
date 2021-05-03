function removeRow(e){
	e.preventDefault();
	$(e.target).parent().parent().parent().remove();
}


////////////////   table 1  section B   /////////////

$(document).ready(function () {
	var newAcademicsNo = 1;
		var newIn ='<tr class="appliRow' + newAcademicsNo + '" id="field1"> <td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="course' + newAcademicsNo +'" id="course' + newAcademicsNo +'" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Enter Course" required></td><td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="course' + newAcademicsNo + '-name" id="course' + newAcademicsNo + '-name" style="margin: 0; background-color: transparent; border:none;" placeholder="Name of Board/College/University"  required></td><td class="col-1" style="text-align: center; padding: 0;">'+
		'<input type="text" name="course' + newAcademicsNo + '-percentage" id="course' + newAcademicsNo + '-percentage" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="% of Marks" required></td><td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="course' + newAcademicsNo + '-subject" id="course' + newAcademicsNo + '-subject" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Subject(s)" required></td><td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;">'+
		'<select name="yearOfPassing'+ newAcademicsNo +'" id="yearOfPassing'+ newAcademicsNo +'" ></select></td><td class="col-3" style="display:flex;place-content:space-between">'+
		'<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>'+
		'<span style="display:inline"><button onclick="removeRow(event)" class="btn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;"></button></span>'+
		'</td></tr>';
	$('.academic-tbody').append(newIn);

  // console.log("hvgvcvdgcvdvcgdvc");
  var yearId ='yearOfPassing' + parseInt(newAcademicsNo);
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

$(document).ready(function () {
	var newAcademicsNo = 2;
	$('.add-more').on('click touchstart',  function (e) {
		e.preventDefault();
		var newIn ='<tr class="appliRow' + newAcademicsNo + '" id="field1"> <td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="course' + newAcademicsNo +'" id="course' + newAcademicsNo +'" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Enter Course" required></td><td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="course' + newAcademicsNo + '-name" id="course' + newAcademicsNo + '-name" style="margin: 0; background-color: transparent; border:none;" placeholder="Name of Board/College/University"  required></td><td class="col-1" style="text-align: center; padding: 0;">'+
		'<input type="text" name="course' + newAcademicsNo + '-percentage" id="course' + newAcademicsNo + '-percentage" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="% of Marks" required></td><td class="col-2" style="text-align: center; padding: 0;">'+
		'<input type="text" name="course' + newAcademicsNo + '-subject" id="course' + newAcademicsNo + '-subject" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Subject(s)" required></td><td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;">'+
		'<select name="yearOfPassing'+ newAcademicsNo +'" id="yearOfPassing'+ newAcademicsNo +'" ></select></td><td class="col-3" style="display:flex;place-content:space-between">'+
		'<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>'+
		'<span style="display:inline"><button onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>'+
		'</td></tr>';
	$('.academic-tbody').append(newIn);

  // console.log("hvgvcvdgcvdvcgdvc");
  var yearId ='yearOfPassing' + parseInt(newAcademicsNo);
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

/////////////////////// table 2  section C ////////////

$(document).ready(function () {
  var newAcademicsNo = 2 ;
	$('.add-more2').on('click touchstart',  function (e) {
		e.preventDefault();

		var newIn2 ='<tr id="field1"><td class="col-2" style="text-align: center; padding: 0;">'+
    '<input type="text" name="empname" id="empname" style="margin: 0; background-color: transparent; border:none; " placeholder="Name of Employer/Status of Institute/University (Govt. /Quasi Govt./Autonomous etc.) "></td>'+
    '<td class="col-2" style="text-align: center; padding: 0;"><input type="text" name="post" id="post" style="margin: 0; background-color: transparent; border:none;" placeholder="Post held / Design"></td>'+
   '<td class="col-1" style="text-align: center; padding: 0;">'+
   '<div class="row gtr-uniform">'+
      '<div class="col-6" style="text-align: right;"><input type="month" name="poefrom" id="poefrom" style="border: 0; width: 90%; background: transparent; padding: 0; align-self: center;" placeholder="From" ></div>'+
      '<div class="col-6" style="text-align: center;"><input type="month" name="poeto" id="poeto" style="border: 0; width: 90%; background: transparent; padding: 0; align-self: center;" placeholder="From" ></div></div></td>'+
   '<td class="col-2" style="text-align: center; padding: 0;"><input type="text" name="salary" id="salary" style="border: 0; background: transparent;" placeholder="Basic Salary"> </td>'+
   '<td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;"> <input type="text" name="duty" id="duty" style="border: 0; background: transparent;" placeholder="Nature of Duty"></td>'+
   '<td class="col-3" style="display:flex;place-content:space-between;">'+'<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>'+
	 '<span style="display:inline;align-self:center"><button onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>'+
		'</td></tr>';

	  $('.academic-tbody2').append(newIn2);

   });
});

/////////////  table 3  Section D  ///////////

$(document).ready(function () {
  var newAcademicsNo = 2;
	$('.add-more3').on('click touchstart',  function (e) {
		e.preventDefault();

		var newIn3 ='<tr id="field1">'+
    '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="textfield1" id="textfield1" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Title of the Book" ></td>'+
		'<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><select name="textfield2" id="textfield2" style="inline-size: auto;"><option value="Sole author">Sole Author</option><option value="Co-author">Co-author</option></select></td>'+
		'<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><textarea type="text" name="textfield3" id="textfield3" value="" style="margin: 0;" rows="2" placeholder="" > </textarea></td>'+
		'<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="month" name="bookDate" id="bookDate" style="width: 75%;"></td>'+
		'<td class="col-2" style="text-align: center; padding: 0; font-size:xx-small;vertical-align: middle;"><input type="text" name="textfield6" id="textfield6" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="ISBN/ISSN No."></td>'+
    '<td class="col-3" style="display:flex;place-content:space-between;height:5em;">'+'<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>'+
	  '<span style="display:inline;align-self:center"><button onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>'+
		'</td></tr>';

	$('.academic-tbody4').append(newIn3);

   });
});


//////////////////  table 4  section d    /////////////////////////////

$(document).ready(function () {
  var newAcademicsNo = 2 ;
	$('.add-more4').on('click touchstart',  function (e) {
		e.preventDefault();
		var newIn4 ='<tr id="field1"><td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="" id="" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Title of the Chapter(s) "></td>'+
  '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"> <input type="text" name="" id="" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none; " placeholder="Title of the Title(s) "></td>'+
  '<td class="col-2" style="text-align: center;vertical-align: middle;padding:0;"> <select name="region3" id="region3" style="background-color: transparent; border:none;inline-size: auto;"> <option value="Sole author">Sole Author</option><option value="Co-author">Co-author</option></select></td>'+
  '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><textarea name="" id="" cols="10" rows="2"></textarea></td><td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="month" style="width: 75%;" name="" id=""></td>'+
  '<td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;vertical-align: middle;"><input type="text" name="" id="" style="border: 0; background: transparent;" placeholder="ISBN/ISSN No."></td>'+
  '<td class="col-3" style="display:flex;place-content:space-between;height:5em">'+'<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>'+
	'<span style="display:inline;align-self:center"><button type="button" onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>'+
	'</td></tr>';

	$('.academic-tbody5').append(newIn4);

   });
});


////////////////////////     table 5  section d  ////////////

$(document).ready(function () {
  var newAcademicsNo = 2 ;
	$('.add-more5').on('click touchstart',  function (e) {
		e.preventDefault();
		var newIn6 ='<tr id="field1"><td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="" id="" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Title of research"></td>'+
  '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="" id="" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none; " placeholder="Name of journal"></td>'+
  '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><select name="region3" id="region3" style="background-color: transparent; border:none;inline-size: auto;"> <option value="Sole author">Sole Author </option> <option value="Co-author">Co-author</option> </select></td>'+
  '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><textarea name="" id="" cols="10" rows="2" style="text-align:center" placeholder="Month & year"></textarea></td>'+
  '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"> <select name="region3" id="region3" style="background-color: transparent; border:none;"><option value="Sole author">Referred</option><option value="Co-author">Non-Referred</option> </select></td>'+
  '<td class="col-1" style="text-align: center; padding: 0; font-size: xx-small;vertical-align: middle;"><input type="text" name="" id="" style="border: 0; background: transparent;" placeholder="ISBN/ISSN No."> </td>'+
  '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" style="border: 0; background: transparent;" name="" id=""></td>'+
  '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"> <input type="text" style="border: 0; background: transparent;" name="" id=""> </td>'+
  '<td class="col-3" style="display:flex;place-content:space-between;height:5em;">'+'<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>'+
	'<span style="display:inline;align-self:center"><button onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>'+
	'</td></tr>' ;
	$('.academic-tbody6').append(newIn6);

   });
});



///////////////////////////    table 6  section d   //////////////////

$(document).ready(function () {
  var newAcademicsNo = 2 ;
	$('.add-more6').on('click touchstart',  function (e) {
		e.preventDefault();
		var newIn7 ='<tr id="field1"><td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="local1" id="local1" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Title of research article/paper(s)"></td>'+
  '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="local2" id="local2" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Name of the Journal" ></td>'+
  '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="local3" id="local3" value=""style="margin: 0; background-color: transparent; border:none;" placeholder="" ></td>'+
  '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="local4" id="local4" value="" style="margin-bottom: 0.5rem; " placeholder="From" ><input type="text" name="local5" id="local5" value="" style="margin: 0;" placeholder="To" ></td>'+
  '<td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;vertical-align: middle;"><select name="local16" id="local16"> <option value="Yes">Yes</option> <option value="No">No</option> </select></td>'+
  '<td class="col-3" style="display:flex;place-content:space-between;height:6em">'+'<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>'+
	 '<span style="display:inline;align-self:center"><button onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>'+
		'</td></tr>';

	$('.academic-tbody7').append(newIn7);

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

