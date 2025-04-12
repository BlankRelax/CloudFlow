let data = arrayVideos.join('\n');
let blob = new Blob([data], {type: 'text/csv'});
let elem = window.document.createElement('a');
elem.href = window.URL.createObjectURL(blob);
elem.download = 'my_data.csv';
document.body.appendChild(elem);
elem.click();
document.body.removeChild(elem);