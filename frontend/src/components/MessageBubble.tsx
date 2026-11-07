import React from 'react';

interface MessageBubbleProps {
  role: 'user' | 'assistant';
  content: string;
}

export const MessageBubble: React.FC<MessageBubbleProps> = ({ role, content }) => {
  const isUser = role === 'user';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div className={`max-w-[80%] px-4 py-2 rounded-2xl ${
        isUser
          ? 'bg-indigo-600 text-white rounded-br-none'
          : 'bg-slate-100 text-slate-800 rounded-bl-none border border-slate-200'
      }`}>
        <p className="text-sm leading-relaxed">{content}</p>
      </div>
    </div>
  );
};
