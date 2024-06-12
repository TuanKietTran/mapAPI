import { useState } from 'react';

export default function Home() {
  const [start, setStart] = useState('');
  const [end, setEnd] = useState('');
  const [routes, setRoutes] = useState([]);

  const fetchRoutes = async () => {
    const apiUrl = process.env.NEXT_PUBLIC_API_ENDPOINT;
    console.log(`${apiUrl}/api/v1/routes?start=${encodeURIComponent(start)}&end=${encodeURIComponent(end)}`);
    const response = await fetch(`${apiUrl}/api/v1/routes?start=${encodeURIComponent(start)}&end=${encodeURIComponent(end)}`, {
      mode: 'no-cors' // sets the request to no-cors mode
    });
    console.log(response);
    const data = await response.json();
    setRoutes(data.routes);
  };

  return (
    <div className="p-4">
      <div className="mb-4">
        <label htmlFor="start" className="block text-sm font-medium text-gray-700 dark:text-gray-200">Start</label>
        <input
          id="start"
          type="text"
          value={start}
          onChange={(e) => setStart(e.target.value)}
          className="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm dark:bg-gray-800 dark:text-white"
        />
      </div>
      <div className="mb-4">
        <label htmlFor="end" className="block text-sm font-medium text-gray-700 dark:text-gray-200">End</label>
        <input
          id="end"
          type="text"
          value={end}
          onChange={(e) => setEnd(e.target.value)}
          className="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm dark:bg-gray-800 dark:text-white"
        />
      </div>
      <button
        onClick={fetchRoutes}
        className="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      >
        Get Routes
      </button>
      <div className="mt-4">
        {routes.map((route, index) => (
          <div key={index} className="mb-4 p-4 shadow rounded-lg bg-white dark:bg-gray-700">
            <div className="font-bold text-lg text-gray-900 dark:text-white">{route.summary}</div>
            <div className="text-gray-800 dark:text-gray-300">Distance: {route.distance}</div>
            <div className="text-gray-800 dark:text-gray-300">Duration: {route.duration}</div>
            <ul className="list-disc pl-5">
              {route.steps.map((step, stepIndex) => (
                <li key={stepIndex} dangerouslySetInnerHTML={{ __html: step.instruction }} className="text-gray-800 dark:text-gray-300" />
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
