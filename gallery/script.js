const req = new XMLHttpRequest();

req.open("GET", "./image_list.json");
req.send();

req.onload = (evt) => {
  const data = JSON.parse(evt.target.response);

  for (let i = 0, max = data.length; i < max; i++) {
    const div = document.createElement("div");
    div.setAttribute("class", "image");

    div.onclick = function () {
      this.classList.toggle("image-selected");
    };

    div.onmouseover = function () {
      let that = this;
      this.timerId = setTimeout(function () {
        that.classList.add("image-magnified");
      }, 1000);
    };

    div.onmouseout = function () {
      clearTimeout(this.timerId);
      this.classList.remove("image-magnified");
    };

    let img = document.createElement("img");
    img.src = data[i];

    div.appendChild(img);
    document.body.appendChild(div);
  }
};

function selectAll(btn) {
  if (btn.value === "select All") {
    Array.prototype.slice.call(document.querySelectorAll(".image")).forEach((slide) => {
      slide.classList.add("image-selected");
    });
    btn.value = "Unselect All";
  } else {
    Array.prototype.slice.call(document.querySelectorAll(".image")).forEach((slide) => {
      slide.classList.remove("image-selected");
    });
    btn.value = "select All";
  }
}

function slideShow(btn) {
  let images = document.querySelectorAll(".image");
  let index = 0;

  images[0].classList.add("image-magnified");

  let intervalId = setInterval(function () {
    images[index].classList.remove("image-magnified");
    index++;
    if (index < images.length) {
      images[index].classList.add("image-magnified");
    } else {
      clearInterval(intervalId);
    }
  }, 1000);
}

