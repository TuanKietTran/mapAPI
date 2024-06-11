'use client'
import { useState } from 'react';
import Router from 'next/router';

export default function Home() {
  const [start, setStart] = useState('');
  const [end, setEnd] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    Router.push(`/routes?start=${encodeURIComponent(start)}&end=${encodeURIComponent(end)}`);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={start}
          onChange={(e) => setStart(e.target.value)}
          placeholder="Start location"
          required
        />
        <input
          type="text"
          value={end}
          onChange={(e) => setEnd(e.target.value)}
          placeholder="End location"
          required
        />
        <button type="submit">Get Routes</button>
      </form>
    </div>
  );
}
