'use strict';

$(function(){
  // Keep track of last scroll
  var lastScroll = 0;
  var userScrolled = false;

  $(window).scroll(function(event){
    userScrolled = true;
  });
  setInterval(function() {
    if (userScrolled) {

      // Sets the current scroll position
      var st = $(this).scrollTop();
      // Determines up-or-down scrolling
      if (st > lastScroll){
        // function call for downward-scrolling
        // $('.ckata').hide();
        // $('.linked').hide();
        $('header').slideUp('fast');
      }
      else {
        // function call for upward-scrolling
        $('header').slideDown('fast');
        // $('.ckata').fadeIn('fast');
        // $('.linked').fadeIn('fast');
      }
      // Updates scroll position
      lastScroll = st;

      userScrolled = false;
    }
    // delay...
  }, 600);
});

// displays gallery imgs in slide show format
$(function () {
  /* time and transition settings */
  let change_img_time 	= 6000,
    transition_speed	= 400,
    simple_slideshow	= $('#slider'),
    listItems	= simple_slideshow.children('li'),
    listLen	= listItems.length, i	= 0,

    changeList = function () {
      listItems.eq(i).fadeOut(transition_speed, function () {
        i += 1;
        if (i === listLen) {
          i = 0;
        }
        listItems.eq(i).fadeIn(transition_speed);
      });
    };

  listItems.not(':first').hide();
  setInterval(changeList, change_img_time);
});

// function for mobile menu on page ready
$(function(){
  if (!sessionStorage.visited){
    $('.overlay').show();
  } else {
    $('.overlay').hide();
  }

  $('.dropdown-content').hide();

  $('.burger').on('touchstart click', function(){
    if ($('nav').is(':hidden')){
      $('#main-nav').slideDown('fast');
    } else {
      $('#main-nav').slideUp('fast');
    }
  });

  $('.overlay').on('click', function(){
    sessionStorage.visited = true;
    // console.log(visited);
    $('.overlay').fadeOut('slow');
  });

  // hide nav into burger when width is small
  $('#home, #about, #events').on('click', function(){
    if (window.innerWidth <= 739){
      $('#main-nav').slideUp('fast');
    }
  });

  // displays dropdown list on click for mobile
  $('.dropdown').on('touchstart click', function(){
    if ($('.dropdown-content').is(':hidden')){
      // $('#project-list').animate({width: 'toggle'},350);
      $('.dropdown-content').slideDown();
    } else {
      $('.dropdown-content').slideUp();
    }
  });

  // displays project list on click for mobile
  $('.dropdown2').on('touchstart click', function(){
    if ($('.dropdown-content2').is(':hidden')){
      // $('#project-list').animate({width: 'toggle'},350);
      $('.dropdown-content2').slideDown();
    } else {
      $('.dropdown-content2').slideUp();
    }
  });

  // handles projects to display
  // $('.dropdown-content').on('click', function(e){
  //   e.preventDefault();
  //   $('.github').fadeOut();
  //   $('.gallery').fadeOut();
  //   $('.me').fadeOut();
  //
  //   if (e.target.id === 'all'){
  //     $('section').fadeIn();
  //     $('content').fadeIn();
  //   }else{
  //     $('content').hide();
  //     let $select = (e.target.text);
  //     projectView.projectFilter($select);
  //     $('section').fadeIn();
  //   }
  //
  //   $('.dropdown-content').slideUp('fast');
  //
  //   if (window.innerWidth <= 739){
  //     $('#main-nav').slideUp('fast');
  //   }
  // });
});
// localStorage.removeItem(key);
