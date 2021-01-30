// 
// Function for creating message window
// 

// function take 3 argumens (mount point, user name, message, who is messagess owner)
export function message_render (mp, user_name, message, is_user){

    // create section and add class
    let section = document.createElement('section');
    section.classList.add('message');

    // check for message owner and add class
    section.classList.add(is_user ? 'user' : 'bot');

    // create header and add class
    let header = document.createElement('header');
    header.classList.add('message__header');

    // create text header add class and username
    let h3 = document.createElement('h3');
    h3.classList.add('user__name');
    h3.textContent = user_name;

    // create message add class and username
    let message_tag = document.createElement('div');
    message_tag.classList.add('message__content');
    message_tag.textContent = message;

    // mounting DOM elements
    header.append(h3);
    section.append(header,message_tag);
    mp.append(section);
}