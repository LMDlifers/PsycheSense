// pages/data-input.js
import { useState } from 'react';
import Router from 'next/router';

export default function DataInput() {
    const [data, setData] = useState('');

    const handleSubmit = async () => {
        const response = await fetch('/api/analyze_mental_health', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content: data }),
        });
        const result = await response.json();
        Router.push({
            pathname: '/results',
            query: { analysis: JSON.stringify(result) },
        });
    };

    return (
        <div className="container">
            <h1>Input Your Data</h1>
            <textarea
                value={data}
                onChange={(e) => setData(e.target.value)}
                placeholder="Enter your recent social media posts or thoughts here..."
            ></textarea>
            <button onClick={handleSubmit}>Analyze</button>
            <style jsx>{`
                .container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    text-align: center;
                    background-color: #f0f4f8;
                }
                textarea {
                    width: 80%;
                    height: 200px;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    margin-bottom: 20px;
                }
                button {
                    padding: 10px 20px;
                    background-color: #0070f3;
                    color: #fff;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
            `}</style>
        </div>
    );
}
