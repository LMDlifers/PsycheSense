// pages/api/fetch_data.js
import fetch from 'node-fetch';

export default async function handler(req, res) {
    const data = [
        { content: "I am feeling very stressed and anxious lately." },
        { content: "Life has been really hard these days." },
        // Add more posts as needed
    ];
    res.status(200).json(data);
}
