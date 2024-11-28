'use client';

import Navbar from '@/components/menu';
import Board from '@/components/board';
import '@/app/globals.css';

export default function Home() {
  return (
    <div className="h-screen ew-full bg-neutral-50 text-neutral-900">
      <Navbar />
      <main>
        <Board />
      </main>
    </div>
  );
}
