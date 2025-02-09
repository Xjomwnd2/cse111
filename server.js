const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Python Portfolio Server Running');
});

// Route to execute Python scripts
app.post('/execute-python', (req, res) => {
    const { script, params } = req.body;
    const pythonProcess = spawn('python', [script, ...params]);
    
    let dataString = '';
    
    pythonProcess.stdout.on('data', (data) => {
        dataString += data.toString();
    });
    
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });
    
    pythonProcess.on('close', (code) => {
        res.json({ result: dataString, code: code });
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});