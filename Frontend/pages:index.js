// pages/index.js
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
