import { render, screen } from '@testing-library/react';
import App from './App';

test('renders get started message', () => {
  render(<App />);
  const linkElement = screen.getByText(/Get started/i);
  expect(linkElement).toBeInTheDocument();
});
