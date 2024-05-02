const express = require('express');
const multer  = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const upload = multer({ dest: '/workspaces/video_main/video_files' });

app.get('/', (req, res) => {
    res.send(`
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="video">
            <input type="text" name="newName" placeholder="Enter new name for the video">
            <button type="submit">Upload</button>
        </form>
    `);
});

app.post('/upload', upload.single('video'), (req, res) => {
    let newName = req.body.newName;
    let oldPath = req.file.path;
    let newPath = path.join('/workspaces/video_main/video_files', newName + path.extname(req.file.originalname));

    fs.rename(oldPath, newPath, function (err) {
        if (err) throw err;
        res.send('File uploaded and renamed!');
    });
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});