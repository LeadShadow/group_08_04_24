const images_list = document.querySelectorAll(".imageSlider");
const point_list = document.querySelectorAll(".point");
const button_arrow_left = document.getElementById("leftBtn");
const button_arrow_right = document.getElementById("rightBtn");
let current_image = 0;

const renderImage = () => {
  if (current_image < 0) {
    current_image = images_list.length - 1;
  } else if (current_image > images_list.length - 1) {
    current_image = 0;
  } else {
  }
  images_list.forEach((image) => {
    image.style.display = "none";
  });
  images_list[current_image].style.display = "block";
};

renderImage();

const pointClickHandler = (index) => {
  current_image = index;
  renderImage();
};
const btnLeftClickHandler = () => {
  current_image -= 1;
  renderImage();
};

const btnRightClickHandler = () => {
  current_image += 1;
  renderImage();
};

point_list.forEach((point, index) => {
  point.addEventListener("click", () => {
    pointClickHandler(index);
  });
});

const autoChangeImage = () => {
  current_image += 1;
  renderImage();
};

setInterval(autoChangeImage, 3000);
button_arrow_left.addEventListener("click", btnLeftClickHandler);
button_arrow_right.addEventListener("click", btnRightClickHandler);
