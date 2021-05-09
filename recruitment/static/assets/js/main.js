function removeRow(e) {
    e.preventDefault();
    $(e.target).parent().parent().parent().remove();
}

function changeReservation(e){
    document.getElementById("reservation_certificate").disabled = false;
}
function changeReservation2(e){
    document.getElementById("reservation_certificate").disabled = true;
}

function sameAddress(e){
    // document.getElementById("permanentaddress").nodeValue = document.getElementById("mailingaddress").nodeValue;
    //console.log("dsfsdas");

    if(document.getElementById("sameaddress").checked==true){
    $('#permanentaddress').val($('#mailingaddress').val());
    $('#permanentpincode').val($('#mailingpincode').val());
    $('#permanenttelephone').val($('#mailingtelephone').val());

    document.getElementById("permanentaddress").readOnly = true;
    document.getElementById("permanentpincode").readOnly = true;
    document.getElementById("permanenttelephone").readOnly = true;
    document.getElementById("mailingaddress").readOnly = true;
    document.getElementById("mailingpincode").readOnly = true;
    document.getElementById("mailingtelephone").readOnly = true;
    }

    else{
    document.getElementById("permanentaddress").readOnly = false;
    document.getElementById("permanentpincode").readOnly = false;
    document.getElementById("permanenttelephone").readOnly = false;
    document.getElementById("mailingaddress").readOnly = false;
    document.getElementById("mailingpincode").readOnly = false;
    document.getElementById("mailingtelephone").readOnly = false;
    }

}

$('form input').keydown(function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        return false;
    }
});



////////////////   table 1  section B   ///////////////

$(document).ready(function() {
    var newAcademicsNo = 1;
    var newIn = '<tr class="appliRow' + newAcademicsNo + '" id="field1"> <td class="col-2" style="text-align: center; padding: 0;">' +
        '<input type="text" name="course' + newAcademicsNo + '" id="course' + newAcademicsNo + '" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Enter Course" required></td><td class="col-2" style="text-align: center; padding: 0;">' +
        '<input type="text" name="course' + newAcademicsNo + '-name" id="course' + newAcademicsNo + '-name" style="margin: 0; background-color: transparent; border:none;" placeholder="Name of Board/College/University"  required></td><td class="col-1" style="text-align: center; padding: 0;">' +
        '<input type="text" name="course' + newAcademicsNo + '-percentage" id="course' + newAcademicsNo + '-percentage" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="% of Marks" required></td><td class="col-2" style="text-align: center; padding: 0;">' +
        '<input type="text" name="course' + newAcademicsNo + '-subject" id="course' + newAcademicsNo + '-subject" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Subject(s)" required></td><td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;">' +
        '<select style="inline-size: auto; " name="yearOfPassing' + newAcademicsNo + '" id="yearOfPassing' + newAcademicsNo + '" ></select></td><td class="col-3" style="display:flex;place-content:space-between">' +
        '<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>' +
        '</td></tr>';
    $('.academic-tbody').append(newIn);

    $("form input").keydown(function (e) {
        if (e.keyCode === 13) {
          e.preventDefault();
          return false;
        }
      });

    // console.log("hvgvcvdgcvdvcgdvc");
    var yearId = 'yearOfPassing' + parseInt(newAcademicsNo);
    var ele = document.getElementById(yearId);
    console.log(ele);
    var presYear = new Date();
    for (let i = presYear.getFullYear(); i >= 1950; i--) {
        // console.log(i);
        var op = document.createElement('option');
        op.value = i;
        op.textContent = i;
        ele.appendChild(op);
        // ele.innerHTML += '<option value=' + i + '>' + i + '</option>\n'
    }
    newAcademicsNo += 1;
});


$(document).ready(function() {
    var newAcademicsNo = 2;
    $('.add-more').on('click touchstart', function(e) {
        e.preventDefault();
        var newIn = '<tr class="appliRow' + newAcademicsNo + '" id="field1"> <td class="col-2" style="text-align: center; padding: 0;">' +
            '<input type="text" name="course' + newAcademicsNo + '" id="course' + newAcademicsNo + '" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Enter Course" required></td><td class="col-2" style="text-align: center; padding: 0;">' +
            '<input type="text" name="course' + newAcademicsNo + '-name" id="course' + newAcademicsNo + '-name" style="margin: 0; background-color: transparent; border:none;" placeholder="Name of Board/College/University"  required></td><td class="col-1" style="text-align: center; padding: 0;">' +
            '<input type="text" name="course' + newAcademicsNo + '-percentage" id="course' + newAcademicsNo + '-percentage" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="% of Marks" required></td><td class="col-2" style="text-align: center; padding: 0;">' +
            '<input type="text" name="course' + newAcademicsNo + '-subject" id="course' + newAcademicsNo + '-subject" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Subject(s)" required></td><td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;">' +
            '<select style="inline-size: auto;" name="yearOfPassing' + newAcademicsNo + '" id="yearOfPassing' + newAcademicsNo + '" ></select></td><td class="col-3" style="display:flex;place-content:space-between">' +
            '<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="course' + newAcademicsNo + '-file" name="course' + newAcademicsNo + '-file"></span>' +
            '<span style="display:inline"><button type="button" onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>' +
            '</td></tr>';
        $('.academic-tbody').append(newIn);

        $('form input').keydown(function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                return false;
            }
        });

        var yearId = 'yearOfPassing' + parseInt(newAcademicsNo);
        var ele = document.getElementById(yearId);
        console.log(ele);
        var presYear = new Date();
        for (let i = presYear.getFullYear(); i >= 1950; i--) {
            var op = document.createElement('option');
            op.value = i;
            op.textContent = i;
            ele.appendChild(op);
        }
        newAcademicsNo += 1;
    });

});


/////////////////////// table 2  section C /////////////////

$(document).ready(function() {
    var newAcademicsNo = 2;
    $('.add-more2').on('click touchstart', function(e) {
        e.preventDefault();

        var newIn2 = '<tr id="field1"><td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;">' +
            '<input type="text" name="org' + newAcademicsNo + '-name" id="org' + newAcademicsNo + '-name" style="margin: 0; background-color: transparent; border:none; " placeholder="Name of Employer/Status of Institute/University (Govt. /Quasi Govt./Autonomous etc.) "></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="org' + newAcademicsNo + '-post" id="org' + newAcademicsNo + '-post" style="margin: 0; background-color: transparent; border:none;" placeholder="Post held / Design"></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;">'+
            '<div class="row gtr-uniform" style="padding: 0.3em;">'+
                '<div class="col-2">From:</div>'+
                '<div class="col-10"><input type="date" name="org' + newAcademicsNo + '-from" id="org' + newAcademicsNo + '-from" value="" style="margin-bottom: 0.5rem;width:95%;background-color: transparent;margin-left: 0.6rem;font-size: small;" placeholder="From"></div>'+
                '<div class="col-2" style="padding-top: 0;">To:</div>'+
                '<div class="col-10" style="padding-top: 0;"><input type="date" name="org' + newAcademicsNo + '-to" id="org' + newAcademicsNo + '-to" value="" style="margin: 0;width:95%;background-color: transparent;margin-left: 0.6rem;font-size: small;" placeholder="To"></div>'+
            '</div></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="org' + newAcademicsNo + '-salary" id="org' + newAcademicsNo + '-salary" style="border: 0; background: transparent;" placeholder="Basic Salary"> </td>' +
            '<td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;vertical-align: middle;"> <input type="text" name="org' + newAcademicsNo + '-nature" id="org' + newAcademicsNo + '-nature" style="border: 0; background: transparent;" placeholder="Nature of Duty"></td>' +
            '<td class="col-3" style="display:flex;place-content:space-between;height:6em;">' + '<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="org' + newAcademicsNo + '-file" name="org' + newAcademicsNo + '-file"></span>' +
            '<span style="display:inline;align-self:center"><button type="button" onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>' +
            '</td></tr>';

        $('.academic-tbody2').append(newIn2);

        $('form input').keydown(function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                return false;
            }
        });

    });
});


/////////////////////// table 2B  section C /////////////////

$(document).ready(function() {
    var newAcademicsNo = 2;
    $('.add-more2B').on('click touchstart', function(e) {
        e.preventDefault();

        var newIn2 = '<tr id="field1">' +
            '<td class="col-2" style="text-align: center;vertical-align: middle;"><input type="date" name="exper' + newAcademicsNo + '-from" id="exp' + newAcademicsNo + '-from" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none; " placeholder="From "></td>' +
            '<td class="col-2" style="text-align: center;vertical-align: middle;"><input type="date" name="exper' + newAcademicsNo + '-to" id="exp' + newAcademicsNo + '-to" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none; " placeholder="To"></td>' +
            '<td class="col-3" style="text-align: center;vertical-align: middle;"> <input type="text" name="exper' + newAcademicsNo + '-months" id="exp' + newAcademicsNo + '-months" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none; " placeholder="Number of Months"></td>' +
            '<td class="col-3" style="display:flex;place-content:space-between;height:4.4em;">' + '<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" id="exp' + newAcademicsNo + '-file" name="exper' + newAcademicsNo + '-file"></span>' +
            '<span style="display:inline;align-self:center"><button onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>' +
            '</td></tr>';

        $('.academic-tbody3').append(newIn2);

        $('form input').keydown(function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                return false;
            }
        });

    });
});


/////////////  table 3  Section D  ///////////////

$(document).ready(function() {
    var newAcademicsNo = 2;
    $('.add-more3').on('click touchstart', function(e) {
        e.preventDefault();

        var newIn3 = '<tr id="field1">' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="books' + newAcademicsNo + '-title" id="books' + newAcademicsNo + '-title" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Title of the Book" ></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><select name="books' + newAcademicsNo + '-author" id="books' + newAcademicsNo + '-author" style="inline-size: auto;"><option value="First author">First Author</option><option value="Co-author">Co-author</option></select></td>' +
            '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><textarea type="text" name="books' + newAcademicsNo + '-publisher" id="books' + newAcademicsNo + '-publisher" value="" style="margin: 0;" rows="2" placeholder="" > </textarea></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="date" name="books' + newAcademicsNo + '-date" id="books' + newAcademicsNo + '-date" style="width:95%;background-color: transparent;margin-left: 0.3rem;"></td>' +
            '<td class="col-2" style="text-align: center; padding: 0; font-size:xx-small;vertical-align: middle;"><input type="text"name="books' + newAcademicsNo + '-number" id="books' + newAcademicsNo + '-number" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="ISBN/ISSN No."></td>' +
            '<td class="col-3" style="display:flex;place-content:space-between;height:5em;">' + '<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" name="books' + newAcademicsNo + '-file" id="books' + newAcademicsNo + '-file"></span>' +
            '<span style="display:inline;align-self:center"><button type="button"  onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>' +
            '</td></tr>';

        $('.academic-tbody4').append(newIn3);

        $('form input').keydown(function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                return false;
            }
        });

    });
});


//////////////////  table 4  section d    ////////////////////

$(document).ready(function() {
    var newAcademicsNo = 2;
    $('.add-more4').on('click touchstart', function(e) {
        e.preventDefault();
        var newIn4 = '<tr id="field1"><td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="chapters' + newAcademicsNo + '-book_title" id="chapters' + newAcademicsNo + '-book_title" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Title of the Chapter(s) "></td>' +
            '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"> <input type="text" name="chapters' + newAcademicsNo + '-chapter" id="chapters' + newAcademicsNo + '-chapter" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none; " placeholder="Title of the Title(s) "></td>' +
            '<td class="col-2" style="text-align: center;vertical-align: middle;padding:0;"> <select name="chapters' + newAcademicsNo + '-author" id="chapters' + newAcademicsNo + '-author" style="background-color: transparent; border:none;inline-size: auto;"> <option value="First author">First Author</option><option value="Co-author">Co-author</option></select></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><textarea name="chapters' + newAcademicsNo + '-publisher" id="chapters' + newAcademicsNo + '-publisher" cols="10" rows="2"></textarea></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="date" style="width:95%;background-color: transparent;margin-left: 0.3rem;" name="chapters' + newAcademicsNo + '-date_of_publisher" id="chapters' + newAcademicsNo + '-date_of_publisher"></td>' +
            '<td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;vertical-align: middle;"><input type="text" name="chapters' + newAcademicsNo + '-number" id="chapters' + newAcademicsNo + '-number" style="border: 0; background: transparent;" placeholder="ISBN/ISSN No."></td>' +
            '<td class="col-3" style="display:flex;place-content:space-between;height:5em">' + '<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" name="chapters' + newAcademicsNo + '-file" id="chapters' + newAcademicsNo + '-file"></span>' +
            '<span style="display:inline;align-self:center"><button  type="button" type="button" onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>' +
            '</td></tr>';

        $('.academic-tbody5').append(newIn4);

        $('form input').keydown(function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                return false;
            }
        });

    });
});


////////////////////////     table 5  section d  ////////////

$(document).ready(function() {
    var newAcademicsNo = 2;
    $('.add-more5').on('click touchstart', function(e) {
        e.preventDefault();
        var newIn6 = '<tr id="field1"><td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="news_articles' + newAcademicsNo + '-article_title" id="news_articles' + newAcademicsNo + '-article_title" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none;" placeholder="Title of research"></td>' +
            '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="news_articles' + newAcademicsNo + '-journal_name" id="news_articles' + newAcademicsNo + '-journal_name" style="margin: 0; background-color: transparent; border:none; background-color: transparent; border: none; " placeholder="Name of journal"></td>' +
            '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><select name="news_articles' + newAcademicsNo + '-author" id="news_articles' + newAcademicsNo + '-author" style="background-color: transparent; border:none;inline-size: auto;"> <option value="First author">First Author </option> <option value="Co-author">Co-author</option> </select></td>' +
            '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="date" name="news_articles' + newAcademicsNo + '-date_published" id="news_articles' + newAcademicsNo + '-date_published" style="inline-size: 9em;padding:0;text-align: center;background-color: transparent;"></td>' +
            '<td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;vertical-align: middle;"><input type="text" name="news_articles' + newAcademicsNo + '-page" id="news_articles' + newAcademicsNo + '-page" style="border: 0; background: transparent;" placeholder="Volume no. & Page nos."></td>' +
            '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><select name="news_articles' + newAcademicsNo + '-referred" id="news_articles' + newAcademicsNo + '-referred"	style="background-color: transparent; border:none;">' +
            '<option value="SCI/SSCI/SCI(E)/ABDC">SCI/SSCI/SCI(E)/ABDC</option>' +
            '<option value="Non (SCI/SSCI/SCI(E)/ABDC)">Non (SCI/SSCI/SCI(E)/ABDC)</option>' +
            '</select></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" style="border: 0; background: transparent;" name="news_articles' + newAcademicsNo + '-impact" id="news_articles' + newAcademicsNo + '-impact" placeholder="Impact Factor"> </td>' +
            '<td class="col-3" style="display:flex;place-content:space-between;padding:0.48em;">' + '<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" name="news_articles' + newAcademicsNo + '-file" id="news_articles' + newAcademicsNo + '-file"></span>' +
            '<span style="display:inline;align-self:center"><button type="button" onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>' +
            '</td></tr>';
        $('.academic-tbody6').append(newIn6);

        $('form input').keydown(function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                return false;
            }
        });

    });
});



///////////////////////////    table 6  section d   //////////////////

$(document).ready(function() {
    var newAcademicsNo = 2;
    $('.add-more6').on('click touchstart', function(e) {
        e.preventDefault();
        var newIn7 = '<tr id="field1"><td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="semi_articles' + newAcademicsNo + '-article_title" id="semi_articles' + newAcademicsNo + '-article_title" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Title of research article/paper(s)"></td>' +
            '<td class="col-2" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="semi_articles' + newAcademicsNo + '-seminar_subject" id="semi_articles' + newAcademicsNo + '-seminar_subject" value="" style="margin: 0; background-color: transparent; border:none;" placeholder="Subject of Conference" ></td>' +
            '<td class="col-1" style="text-align: center; padding: 0;vertical-align: middle;"><input type="text" name="semi_articles' + newAcademicsNo + '-location" id="semi_articles' + newAcademicsNo + '-location" value=""style="margin: 0; background-color: transparent; border:none;" placeholder="Organizing Institution" ></td>' +
            '<td class="col-2"style="text-align: center; padding: 0;vertical-align: middle;">' +
            '<div class="row gtr-uniform" style="padding: 0.3em;">' +
            '<div class="col-2">From:</div>' +
            '<div class="col-10"><input type="date" name="semi_articles' + newAcademicsNo + '-from" id="semi_articles' + newAcademicsNo + '-from" value="" style="margin-bottom: 0.5rem;width:95%;background-color: transparent;margin-left: 0.6rem;font-size: small;"></div>' +
            '<div class="col-2" style="padding-top: 0;">To:</div>' +
            '<div class="col-10" style="padding-top: 0;"><input type="date" name="semi_articles' + newAcademicsNo + '-to" id="semi_articles' + newAcademicsNo + '-to" value="" style="margin: 0;width:95%;background-color: transparent;margin-left: 0.6rem;font-size: small;"></div>' +
            '</div></td>' +
            '<td class="col-2" style="text-align: center; padding: 0; font-size: xx-small;vertical-align: middle;"><select name="semi_articles' + newAcademicsNo + '-published" id="semi_articles' + newAcademicsNo + '-published"> <option value="Yes">Yes</option> <option value="No">No</option> </select></td>' +
            '<td class="col-3" style="display:flex;place-content:space-between;height:6em;padding:0;">' + '<span style="overflow:hidden;align-self:center"><input style="font-size:x-small;" type="file" name="semi_articles' + newAcademicsNo + '-file" id="semi_articles' + newAcademicsNo + '-file"></span>' +
            '<span style="display:inline;align-self:center"><button type="button" onclick="removeRow(event)" class="btn remBtn" style="padding: 0;height: 0 !important;min-width:auto!important;margin:0!important;width: 2rem !important;font-size: 0.8em;color: #c514148a !important;">X</button></span>' +
            '</td></tr>';

        $('.academic-tbody7').append(newIn7);

        $('form input').keydown(function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                return false;
            }
        });

    });
});


function openNav() {
    document.getElementById("myNav").style.height = "100%";
}

function closeNav() {
    document.getElementById("myNav").style.height = "0%";
}



(function($) {
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
    $window.on('load', function() {
        window.setTimeout(function() {
            $body.removeClass('is-preload');
        }, 100);
    });

    // Nav.
    var $nav = $('#nav');

    if ($nav.length > 0) {
        // Shrink effect.
        $main.scrollex({
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
                offset: function() {
                    return $nav.height();
                },
            })
            .on('click', function() {
                var $this = $(this);

                // External link? Bail.
                if ($this.attr('href').charAt(0) != '#') return;

                // Deactivate all links.
                $nav_a.removeClass('active').removeClass('active-locked');

                // Activate link *and* lock it (so Scrollex doesn't try to activate other links as we're scrolling to this one's section).
                $this.addClass('active').addClass('active-locked');
            })
            .each(function() {
                var $this = $(this),
                    id = $this.attr('href'),
                    $section = $(id);

                // No section for this link? Bail.
                if ($section.length < 1) return;

                // Scrollex.
                $section.scrollex({
                    mode: 'middle',
                    initialize: function() {
                        // Deactivate section.
                        if (browser.canUse('transition')) $section.addClass('inactive');
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
$('#profileImage').click(function(e) {
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

$('#imageUpload').change(function() {
    fasterPreview(this);
});



////   Upload Signatures   //////
$('#signImage').click(function(e) {
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

$('#signUpload').change(function() {
    fasterPreview2(this);
});