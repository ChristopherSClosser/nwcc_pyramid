'use strict';

// Hide main nav on scroll down
/*
$(function(){
  // Keep track of last scroll
  let lastScroll = 0;
  let userScrolled = false;

  $(window).scroll(function(event){
    userScrolled = true;
  });
  setInterval(function() {
    if (userScrolled) {

      // Sets the current scroll position
      let st = $(this).scrollTop();
      // Determines up-or-down scrolling
      if (st > lastScroll){
        // function call for downward-scrolling
        $('header').slideUp('fast');
      }
      else {
        // function call for upward-scrolling
        $('header').slideDown('fast');
      }
      // Updates scroll position
      lastScroll = st;

      userScrolled = false;
    }
    // delay...
  }, 600);
});
*/

// displays gallery imgs in slide show format
$(function () {
  /* time and transition settings */
  let change_img_time 	= 6000,
    transition_speed	= 400,
    simple_slideshow	= $('#slider'),
    listItems	= simple_slideshow.children('li'),
    listLen	= listItems.length,
    i	= 0,

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

  $('.burger').on('click', function(){
    if ($('nav').is(':visible')){
      $('#main-nav').slideUp('fast');
    } else {
      $('#main-nav').slideDown('fast');
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

  // displays dropdown list on click
  $('.dropdown').on('click', function(){
    if ($('.dropdown-content').is(':hidden')){
      // $('#project-list').animate({width: 'toggle'},350);
      $('.dropdown-content').slideDown();
    } else {
      $('.dropdown-content').slideUp();
    }
  });

  // displays dropdown list on click
  $('.dropdown2').on('click', function(){
    if ($('.dropdown-content2').is(':hidden')){
      // $('#project-list').animate({width: 'toggle'},350);
      $('.dropdown-content2').slideDown();
    } else {
      $('.dropdown-content2').slideUp();
    }
  });

  //displays volunteer Confirmation and email
  $('#volunteervids').on('click', function(){
    if($('#volcontinue').is(':hidden')){
      $('#volcontinue').show();
    }
  });

  $('#volcontinue').on('click', function(){
    if($('#confirm').is(':hidden')){
      $('#volcontinue').hide();
      $('#confirm').show();
    }
  });

  $('#confirm').on('click', function(){
    if($('#volemail').is(':hidden')){
      $('#confirm').hide();
      $('#volemail').show();
    }
  });

});


// localStorage.removeItem(key);
