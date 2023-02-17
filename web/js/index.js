const video = document.getElementById("video");
const app = document.getElementById("app");
const canvas = document.querySelector("#canvas");

if (navigator.mediaDevices.getUserMedia) {
    const stream = navigator.mediaDevices.getUserMedia({ video: true });
    stream
        .then(function (stream) {
        video.srcObject = stream;
        })
        .catch(function (_) {
        console.log("Something went wrong!");
        });
}

const getPrediction = () => {
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageDataUrl = canvas.toDataURL('image/jpeg');
    download(imageDataUrl, "imagen.jpg");
    setTimeout(() => {
        eel.detect_ear();
    }, 500);
}

const download = (dataurl, filename) => {
    const link = document.createElement("a");
    link.href = dataurl;
    link.download = filename;
    link.click();
}

eel.expose(get_result);
function get_result(message, values) {
    if(message == 0) {
        app.innerHTML = `<p class="error">No es una oreja, favor de colocar su apuntando a la cámara<p/>`;
        setTimeout(() => {
            app.innerHTML = ``;
        }, 8000);
        return;
    }

    if(values == 1) {
        app.innerHTML = `<p class="succes">Acceso concedido<p/>`;
    } else {
        app.innerHTML = `<p class="error">Acceso denegado<p/>`;
    }
    setTimeout(() => {
        app.innerHTML = ``;
    }, 8000);
}