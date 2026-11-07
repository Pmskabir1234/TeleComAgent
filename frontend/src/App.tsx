import { useState, useEffect } from 'react';
import { checkHealth } from './shared/lib/api';

type ConnectivityStatus = 'checking' | 'online' | 'offline';

function App() {
  const [status, setStatus] = useState<ConnectivityStatus>('checking');
  const [version, setVersion] = useState<string | null>(null);

  useEffect(() => {
    async function verifyConnectivity() {
      try {
        const data = await checkHealth();
        setStatus('online');
        setVersion(data.version);
      } catch (error) {
        setStatus('offline');
      }
    }

    verifyConnectivity();
  }, []);

  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4 font-sans">
      <div className="max-w-md w-full bg-white rounded-2xl shadow-xl border border-slate-200 p-8 text-center">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-slate-900 mb-2">
            System Connectivity
          </h1>
          <p className="text-slate-500 text-sm">
            Validating end-to-end pipeline status
          </p>
        </div>

        <div className="flex flex-col items-center justify-center space-y-4">
          <div className="flex items-center space-x-3 px-4 py-2 rounded-full bg-slate-100 border border-slate-200">
            <div className={`w-3 h-3 rounded-full animate-pulse ${
              status === 'online' ? 'bg-emerald-500' :
              status === 'offline' ? 'bg-rose-500' :
              'bg-slate-400'
            }`} />
            <span className="text-sm font-medium text-slate-700">
              {status === 'online' && 'System Online'}
              {status === 'offline' && 'System Offline'}
              {status === 'checking' && 'Connecting to System...'}
            </span>
          </div>

          {status === 'online' && (
            <div className="mt-2 text-xs text-slate-400 font-mono">
              Backend Version: <span className="text-slate-600">{version}</span>
            </div>
          )}
        </div>

        <div className="mt-8 pt-6 border-t border-slate-100">
          <p className="text-xs text-slate-400">
            Infrastructure Validation Phase • Slice 1
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
