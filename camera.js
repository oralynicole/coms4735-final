// Get references to the button and image elements
const captureButton = document.querySelector('#captureButton');
const capturedImage = document.querySelector('#capturedImage');

// Set up the camera access
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    // Set the video stream as the source of the video element
    const video = document.createElement('video');
    video.srcObject = stream;
    document.body.appendChild(video);
    video.play();
  })
  .catch(error => {
    console.error(error);
  });

// Add an event listener to the capture button
captureButton.addEventListener('click', () => {
  // Get a reference to the video element
  const video = document.querySelector('video');

  // Create a canvas element and set its dimensions to match the video element
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  // Draw the current video frame onto the canvas
  const context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);

  // Convert the canvas data to a data URL and set it as the source of the image element
  capturedImage.src = canvas.toDataURL();

  // Save the image
  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'save-image.php', true);
  xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
  xhr.onreadystatechange = () => {
    if (xhr.readyState === 4 && xhr.status === 200) {
      console.log('Image saved successfully');
    }
  };
  xhr.send(JSON.stringify({ imageData: capturedImage.src }));
});
