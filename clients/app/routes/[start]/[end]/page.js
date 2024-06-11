import { useRouter } from 'next/router';

export default function Route({ route }) {
  const router = useRouter();

  if (router.isFallback) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h2>{route.summary} ({route.distance}, {route.duration})</h2>
      <ol>
        {route.steps.map((step, index) => (
          <li key={index} dangerouslySetInnerHTML={{__html: step.instruction}} />
        ))}
      </ol>
    </div>
  );
}

export async function getStaticPaths() {
  // Example predefined paths
  return {
    paths: [
      { params: { start: 'NewYork', end: 'LosAngeles' } },
      { params: { start: 'Chicago', end: 'Seattle' } },
    ],
    fallback: true, // Can also be 'blocking' to wait for the generation on new paths
  };
}

export async function getStaticProps({ params }) {
  const { start, end } = params;
  const response = await fetch(`http://localhost:8000/routes/?start=${start}&end=${end}`);
  const data = await response.json();

  return {
    props: {
      route: data.routes[0], // Assuming the API returns an array of routes
    },
    revalidate: 3600, // Regenerate the page at most once per hour
  };
}
