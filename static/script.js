function replace_gt_lt(input_str) {
  // Replaces the greater than (>) and less than (<) signs
  // to prevent rendering as HTML

  return input_str.replace(/\</g, "&lt;").replace(/\>/g, "&gt;");
}

function show_results(results, url) {
  // Takes the results from the backend and renders into
  // a HTML template

  output_str = "";

  results.forEach(function (ele) {
    output_str += `<div class="output-result-single">${replace_gt_lt(
      ele
    )}</div>`;
  });

  output_str = `
    <div class="output-box-title">
        Results for <b>${url}</b>:
    </div>
    <div class="output-result-container">
    <button id="copy" type="button" onclick="copyEvent('output-box')">
        Copy
    </button>
        ${output_str}
    </div>`;

  result_box = document.querySelector("#output-box");
  result_box.innerHTML = output_str;
}

function get_results(url, type, selector) {
  // Sends an AJAX request with the inputs and gets back the results

  var httpRequest = new XMLHttpRequest();
  httpRequest.open("POST", "/get_results");

  httpRequest.onreadystatechange = function () {
    if (httpRequest.readyState == XMLHttpRequest.DONE) {
      var resp = httpRequest.responseText;
      resp = JSON.parse(resp);
      // console.log(resp)

      show_results(resp, url);
    }
  };
  httpRequest.onerror = function () {
    console.log("Error loading results");
  };

  form_data = {
    url: url,
    type: type,
    selector: selector,
  };
  payload = JSON.stringify(form_data);
  httpRequest.send(payload);
}

// Form submission, this will trigger the ajax call for clicking submit
document.querySelector("#form-submit").addEventListener("click", function (e) {
  e.preventDefault();

  url = document.querySelector("#url").value;
  type = document.querySelector("#type").value;
  selector = document.querySelector("#selector").value;

  get_results(url, type, selector);
});

type_box = document.querySelector("#type");
selector_box = document.querySelector("#selector");

// This will hide/show the class/ID name box
type_box.addEventListener("change", (event) => {
  if (type_box.value === "class" || type_box.value === "id") {
    selector_box.parentElement.style.display = "block";
  } else {
    selector_box.parentElement.style.display = "none";
  }
});

function copyEvent(id) {
  var str = document.getElementById(id);
  window.getSelection().selectAllChildren(str);
  document.execCommand("Copy");
}
