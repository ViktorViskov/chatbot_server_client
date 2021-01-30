// 
// Js script for sending requests
// 

// 
// Import libs
// 

// request
import { send_request } from "./request.js";

// message render
import { message_render } from "./render.js";


// 
// Start app
// 

// search mount point for messages
let mp = document.querySelector('.main')

// search textarea
let textarea = document.querySelector('.footer__textarea');

// search button
let btn = document.querySelector(".footer__btn")

// add event to button
btn.addEventListener('click', () => {
    
    // print message in chat
    message_render(mp, 'User', textarea.value, true)

    // send request
    send_request(textarea.value, mp);
});
