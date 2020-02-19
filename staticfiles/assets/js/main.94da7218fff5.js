/*
	Stellar by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

$(document).ready(function(){
    var next = 1;
    $(".add-more").click(function(e){
        e.preventDefault();
        var addto = "#field" + next;
        var addRemove = "#field" + (next);
        next = next + 1;
		/*var newIn = '<input autocomplete="off" class="input form-control" id="field' + next + '" name="field' + next + '" type="text">';*/
		var newIn = '<tr class="row gtr-0" id="field'+next+'"><td class="col-2 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="degree'+next+'" id="degree'+next+'" value="" style="margin: 0;" placeholder="" required></td><td class="col-2 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="qual'+next+'" id="qual'+next+'" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="cat_univ'+next+'" id="cat_univ'+next+'" value="" style="margin: 0;" placeholder="" required></td><td class="col-2 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="institute'+next+'" id="institute'+next+'" value="" style="margin: 0;" placeholder="" required><td><td class="col-2 col-12-small" style="text-align: center; padding: 0; font-size: xx-small;"><select name="status'+next+'" id="status'+next+'"><option value="Completed">Completed</option><option value="ResultAwaited">Results Awaited</option><option value="FinalAwaited">Finals Awaited</option><option value="Ongoing">Ongoing</option></select></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="pass'+next+'" id="pass1" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="marks'+next+'" id="marks'+next+'" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><button id="b'+next+'" class="but add-more" style="padding: 0%; width: 8.333333%; height: auto;">+</button></td></tr>'
        var newInput = $(newIn);
        var removeBtn = '<button id="remove' + (next - 1) + '" class="but btn-danger remove-me" >-</button></td><tr id="field'+(next-1)+'">';
        var removeButton = $(removeBtn);
        $(addto).after(newInput);
        $(addRemove).after(removeButton);
        $("#field" + next).attr('data-source',$(addto).attr('data-source'));
        $("#count").val(next);
		$('.remove-me').click(function(e){
			e.preventDefault();
			var fieldNum = this.id.charAt(this.id.length-1);
			var fieldID = "#field" + fieldNum;
			$(this).remove();
			$(fieldID).remove();
		});
	});
	var nextProfession = 1
    $(".add-more2").click(function(e){
        e.preventDefault();
        var addto = "#profession" + nextProfession;
        var addRemove = "#profession" + (nextProfession);
        nextProfession = nextProfession + 1;
		/*var newIn = '<input autocomplete="off" class="input form-control" id="field' + nextProfession + '" name="field' + nextProfession + '" type="text">';*/
		var newIn = '<tr class="row gtr-0" id="profession'+nextProfession+'"><td class="col-2 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;">	<input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-2 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="active"><button id="bu'+nextProfession+'" class="btn add-more2" style="padding: 0%;">+</button></td></tr>'
        var newInput = $(newIn);
        var removeBtn = '<button id="remove' + (nextProfession - 1) + '" class="btn btn-danger remove-me" >-</button></td><tr id="profession'+(nextProfession-1)+'">';
        var removeButton = $(removeBtn);
        $(addto).after(newInput);
        $(addRemove).after(removeButton);
        $("#profession" + nextProfession).attr('data-source',$(addto).attr('data-source'));
        $("#count").val(nextProfession);
		$('.remove-me').click(function(e){
			e.preventDefault();
			var fieldNum = this.id.charAt(this.id.length-1);
			var fieldID = "#profession" + fieldNum;
			$(this).remove();
			$(fieldID).remove();
		});
    });
	var nextTeach = 1
    $(".add-more3").click(function(e){
        e.preventDefault();
        var addto = "#teach" + nextTeach;
        var addRemove = "#teach" + (nextTeach);
        nextTeach = nextTeach + 1;
		/*var newIn = '<input autocomplete="off" class="input form-control" id="field' + nextTeach + '" name="field' + nextTeach + '" type="text">';*/
		var newIn = '<tr class="row gtr-0" id="teach'+nextTeach+'"><td class="col-2 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;">	<input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-2 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="col-1 col-12-small" style="text-align: center; padding: 0;"><input type="text" name="sschool" id="sschool" value="" style="margin: 0;" placeholder="" required></td><td class="active"><button id="bu'+nextTeach+'" class="btn add-more2" style="padding: 0%;">+</button></td></tr>'
        var newInput = $(newIn);
        var removeBtn = '<button id="remove' + (nextTeach - 1) + '" class="btn btn-danger remove-me" >-</button></td><tr id="teach'+(nextTeach-1)+'">';
        var removeButton = $(removeBtn);
        $(addto).after(newInput);
        $(addRemove).after(removeButton);
        $("#teach" + nextTeach).attr('data-source',$(addto).attr('data-source'));
        $("#count").val(nextTeach);
		$('.remove-me').click(function(e){
			e.preventDefault();
			var fieldNum = this.id.charAt(this.id.length-1);
			var fieldID = "#teach" + fieldNum;
			$(this).remove();
			$(fieldID).remove();
		});
    });
});

(function($) {

	var	$window = $(window),
		$body = $('body'),
		$main = $('#main');

	// Breakpoints.
		breakpoints({
			xlarge:   [ '1281px',  '1680px' ],
			large:    [ '981px',   '1280px' ],
			medium:   [ '737px',   '980px'  ],
			small:    [ '481px',   '736px'  ],
			xsmall:   [ '361px',   '480px'  ],
			xxsmall:  [ null,      '360px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Nav.
		var $nav = $('#nav');

		if ($nav.length > 0) {

			// Shrink effect.
				$main
					.scrollex({
						mode: 'top',
						enter: function() {
							$nav.addClass('alt');
						},
						leave: function() {
							$nav.removeClass('alt');
						},
					});

			// Links.
				var $nav_a = $nav.find('a');

				$nav_a
					.scrolly({
						speed: 1000,
						offset: function() { return $nav.height(); }
					})
					.on('click', function() {

						var $this = $(this);

						// External link? Bail.
							if ($this.attr('href').charAt(0) != '#')
								return;

						// Deactivate all links.
							$nav_a
								.removeClass('active')
								.removeClass('active-locked');

						// Activate link *and* lock it (so Scrollex doesn't try to activate other links as we're scrolling to this one's section).
							$this
								.addClass('active')
								.addClass('active-locked');

					})
					.each(function() {

						var	$this = $(this),
							id = $this.attr('href'),
							$section = $(id);

						// No section for this link? Bail.
							if ($section.length < 1)
								return;

						// Scrollex.
							$section.scrollex({
								mode: 'middle',
								initialize: function() {

									// Deactivate section.
										if (browser.canUse('transition'))
											$section.addClass('inactive');

								},
								enter: function() {

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

								}
							});

					});

		}

	// Scrolly.
		$('.scrolly').scrolly({
			speed: 1000
		});

})(jQuery);
