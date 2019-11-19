async function readFileAsBase64(imageInputName, selectedImageId, url, dotNetObjectReference) {
    let photo = document.getElementById(imageInputName).files[0];  // file from input
    let req = new XMLHttpRequest();
    let formData = new FormData();

    formData.append("file", photo);
    req.open("POST", url, true);

    req.onload = function () {
        showImage(selectedImageId, photo);
    };  

    req.onreadystatechange = function () {
        readFileCallback(req, dotNetObjectReference);
    };

    req.send(formData);
};

async function readFileCallback(xmlhttp, dotNetObjectReference) {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var obj = JSON.parse(xmlhttp.responseText);
        var text = "Class: " + obj.className + " - " + "Confidence: " + obj.confidence;
        console.log(text);
        dotNetObjectReference.invokeMethodAsync('SetResult', obj);
    }
}

async function showImage(imageContainerId, image) {
    var reader = new FileReader();

    reader.onload = function (e) {
        $('#' + imageContainerId)
            .attr('src', e.target.result)
            .width("100%")
            .height("100%")
            .removeAttr('hidden');
    };

    reader.readAsDataURL(image);
}

window.methods = {
    readFileAsBase64: function (imageInputName, selectedImageId, url, dotNetObjectReference) {
        return readFileAsBase64(imageInputName, selectedImageId, url, dotNetObjectReference);
    }
}