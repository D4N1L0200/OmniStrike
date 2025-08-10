const wrapper = document.querySelector(".full-screen-wrapper");
const card = wrapper.querySelector(".card");

function scaleCard() {
	if (!card) return;

	const vw = window.innerWidth - 20;
	const vh = window.innerHeight - 20;

	const baseWidth = 250;
	const baseHeight = 350;

	const scaleX = vw / baseWidth;
	const scaleY = vh / baseHeight;

	const scale = Math.min(scaleX, scaleY, 4);

	card.style.transform = `scale(${scale})`;
}

window.addEventListener("resize", scaleCard);
window.addEventListener("load", scaleCard);
