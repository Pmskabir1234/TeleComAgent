import React, { useState, useEffect, useRef } from 'react';
import { checkHealth } from './shared/lib/api';
import { MessageBubble } from './components/MessageBubble';
import { ChatInput } from './components/ChatInput';

// Extend the api.ts functionality internally for chat
async function sendMessage(conversationId: number | null, text: string) {
  const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';
  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ conversation_id: conversationId, message: text }),
  });

  if (!response.ok) throw new Error('Chat request failed');
  return response.json();
}

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

function App() {
  const [status, setStatus] = useState<'checking' | 'online' | 'offline'>('checking');
  const [conversationId, setConversationId] = useState<number | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    async function verifyConnectivity() {
      try {
        await checkHealth();
        setStatus('online');
      } catch (error) {
        setStatus('offline');
      }
    }
    verifyConnectivity();
  }, []);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSend = async (text: string) => {
    setIsLoading(true);
    // Optimistically add user message
    const userMsg: Message = { role: 'user', content: text };
    setMessages(prev => [...prev, userMsg]);

    try {
      const data = await sendMessage(conversationId, text);
      setConversationId(data.conversation_id);
      setMessages(data.messages.map((m: any) => ({
        role: m.role,
        content: m.content
      })));
    } catch (error) {
      console.error('Chat error:', error);
      setMessages(prev => [...prev, { role: 'assistant', content: 'Sorry, I am having trouble connecting to the server.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  if (status === 'offline') {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
        <div className="max-w-md w-full bg-white rounded-2xl shadow-xl border border-rose-200 p-8 text-center">
          <div className="w-12 h-12 bg-rose-100 text-rose-500 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
          </div>
          <h1 className="text-xl font-bold text-slate-900 mb-2">System Offline</h1>
          <p className="text-slate-500 text-sm mb-6">The backend service is currently unreachable. Please ensure the server is running.</p>
          <button
            onClick={() => window.location.reload()}
            className="px-4 py-2 bg-slate-900 text-white rounded-lg text-sm hover:bg-slate-800 transition-colors"
          >
            Retry Connection
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-100 flex items-center justify-center p-4 font-sans">
      <div className="max-w-2xl w-full h-[80vh] bg-white rounded-3xl shadow-2xl border border-slate-200 flex flex-col overflow-hidden">
        {/* Header */}
        <div className="px-6 py-4 bg-white border-b border-slate-100 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="relative">
              <div className="w-10 h-10 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 font-bold">
                TA
              </div>
              <div className={`absolute bottom-0 right-0 w-3 h-3 rounded-full border-2 border-white ${status === 'online' ? 'bg-emerald-500' : 'bg-slate-400'}`} />
            </div>
            <div>
              <h2 className="text-sm font-bold text-slate-900">Telecom AI Assistant</h2>
              <p className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">
                {status === 'online' ? 'Connected' : 'Connecting...'}
              </p>
            </div>
          </div>
        </div>

        {/* Chat Area */}
        <div
          ref={scrollRef}
          className="flex-1 overflow-y-auto p-6 space-y-4 bg-slate-50/50"
        >
          {messages.length === 0 && (
            <div className="h-full flex items-center justify-center text-center p-8">
              <div className="max-w-xs">
                <p className="text-slate-400 text-sm">
                  Welcome to the Telecom AI Assistant. How can I help you with your services today?
                </p>
              </div>
            </div>
          )}
          {messages.map((msg, idx) => (
            <MessageBubble key={idx} role={msg.role} content={msg.content} />
          ))}
          {isLoading && (
            <div className="flex justify-start mb-4">
              <div className="bg-slate-100 text-slate-800 px-4 py-2 rounded-2xl rounded-bl-none border border-slate-200">
                <div className="flex space-x-1">
                  <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                  <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                  <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Input Area */}
        <ChatInput
          onSendMessage={handleSend}
          isLoading={isLoading}
        />
      </div>
    </div>
  );
}

export default App;
