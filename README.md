# PsycheSense Application

## Overview

This application analyzes social media posts to detect signs of mental health issues and provides insights. It uses LlamaIndex for semantic analysis and can integrate with social media platforms' APIs for data collection.


## Features

- Collects social media data from platforms like Twitter, Reddit, and others.
- Preprocesses and embeds the data using LlamaIndex.
- Analyzes the data for signs of mental health issues.
- Provides insights and recommendations based on the analysis.

## Prerequisites

- Python 3.8+
- Node.js (for deploying with Vercel)
- Social media API keys (Twitter, Reddit, Facebook, Instagram, YouTube)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/mental-health-app.git
    cd mental-health-app
    ```

2. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root directory and add your API keys:

    ```env
    TWITTER_CONSUMER_KEY=your_consumer_key
    TWITTER_CONSUMER_SECRET=your_consumer_secret
    TWITTER_ACCESS_TOKEN=your_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

    REDDIT_CLIENT_ID=your_client_id
    REDDIT_CLIENT_SECRET=your_client_secret
    REDDIT_USER_AGENT=your_user_agent

    FACEBOOK_ACCESS_TOKEN=your_access_token

    INSTAGRAM_ACCESS_TOKEN=your_access_token
    INSTAGRAM_USER_ID=your_user_id

    YOUTUBE_API_KEY=your_api_key
    ```

4. **Set up the backend server:**

    ```bash
    python app.py
    ```

5. **Initialize a new Next.js project:**

    ```bash
    npx create-next-app frontend
    cd frontend
    ```

6. **Create API endpoints in Next.js:**

    Add the following files:

    - `pages/api/fetch_data.js`

    ```javascript
    import fetch from 'node-fetch';

    export default async function handler(req, res) {
        const data = [
            { content: "I am feeling very stressed and anxious lately." },
            { content: "Life has been really hard these days." },
            // Add more posts as needed
        ];
        res.status(200).json(data);
    }
    ```

    - `pages/api/analyze_mental_health.js`

    ```javascript
    import { preprocess_data, generate_embeddings, analyze_mental_health } from '../../path_to_your_scripts';

    export default async function handler(req, res) {
        const data = req.body;
        const preprocessed_data = preprocess_data(data);
        const index = generate_embeddings(preprocessed_data);
        const analysis_results = analyze_mental_health(index, "signs of mental health issues");
        res.status(200).json(analysis_results);
    }
    ```

7. **Create frontend pages:**

    - `pages/index.js`

    ```javascript
    import Link from 'next/link';

    export default function Home() {
        return (
            <div className="container">
                <h1>Welcome to the Mental Health App</h1>
                <p>Your well-being is our priority.</p>
                <Link href="/data-input"><button>Get Started</button></Link>
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
                    h1 {
                        color: #333;
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
    ```

    - `pages/data-input.js`

    ```javascript
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
    ```

    - `pages/results.js`

    ```javascript
    import { useRouter } from 'next/router';

    export default function Results() {
        const router = useRouter();
        const { analysis } = router.query;
        const parsedAnalysis = analysis ? JSON.parse(analysis) : {};

        return (
            <div className="container">
                <h1>Analysis Results</h1>
                <pre>{JSON.stringify(parsedAnalysis, null, 2)}</pre>
                <button onClick={() => router.push('/')}>Go Back</button>
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
                    pre {
                        text-align: left;
                        background: #fff;
                        padding: 20px;
                        border-radius: 5px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }
                    button {
                        padding: 10px 20px;
                        background-color: #0070f3;
                        color: #fff;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        margin-top: 20px;
                    }
                `}</style>
            </div>
        );
    }
    ```

### Deployment

1. **Deploy the Backend:**

    You can use any cloud provider like AWS, Google Cloud, or Azure. For simplicity, here's an example using AWS Elastic Beanstalk:

    ```bash
    eb init -p python-3.8 mental-health-app
    eb create mental-health-app-env
    ```

2. **Deploy the Frontend with Vercel:**

    ```bash
    vercel deploy
    ```

## Usage

1. Start the backend server:

    ```bash
    python app.py
    ```

2. Navigate to your Vercel deployment URL to use the frontend interface.

## Security and Privacy

- Ensure HTTPS is used for secure communication.
- Implement authentication and authorization.
- Comply with data protection regulations (e.g., GDPR).

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.
