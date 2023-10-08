// Countdown Timer
const countDownDate = new Date("Oct 20, 2023 19:00:00").getTime();

const x = setInterval(function () {
    const now = new Date().getTime();
    const distance = countDownDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown").innerHTML = days + "d " + hours + "h "
        + minutes + "m " + seconds + "s ";

    if (distance < 0) {
        clearInterval(x);
        document.getElementById("countdown").innerHTML = "EXPIRED";
    }
}, 1000);

// Funky Hover Effect
document.getElementById('details').addEventListener('mouseover', function () {
    this.style.backgroundColor = '#' + (Math.random() * 0xFFFFFF << 0).toString(16);
});

document.getElementById('details').addEventListener('mouseout', function () {
    this.style.backgroundColor = '#E6E6FA';
});
