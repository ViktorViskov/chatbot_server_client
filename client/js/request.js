//
// Function for send AJAX requests
//

// message render
import { message_render } from "./js/render.js";

// function take 2 arguments (quastion and place for message)
export function send_request(data, mp) {
	//
	// Configs
	//

	let url = "http://10.0.0.99:81/bot";
	let method = "post";

	// make request
	let xhr = new XMLHttpRequest();

	// request initialization
	xhr.open(method, url);

	// create header
	xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8');

	// create data to send
	let json = JSON.stringify({message: data});

	// send request
	xhr.send(json);

	// response
	xhr.onload = function () {
		if (xhr.status != 200) {
			console.log("Connection error");
		} else {
			
			// print message
			message_render(mp, 'Bot', xhr.response, false);

			// scrol down
			window.scrollTo(0,document.body.scrollHeight);
		}
	};
}
