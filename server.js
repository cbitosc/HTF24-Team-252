const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());
app.use(cors());

app.post('/calculate-next-cycle', (req, res) => {
    const { startDate } = req.body;
    const cycleLength = 28;

    const start = new Date(startDate);
    const nextCycle = new Date(start);
    nextCycle.setDate(start.getDate() + cycleLength);

    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    res.json({ nextCycleDate: nextCycle.toLocaleDateString(undefined, options) });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
