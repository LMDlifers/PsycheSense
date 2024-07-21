// pages/results.js
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
