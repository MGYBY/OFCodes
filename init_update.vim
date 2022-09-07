"set runtimepath^=~/.vim runtimepath+=~/.vim/after

"let &packpath = &runtimepath

"source ~/.vimrc
"
"let g:coc_node_path = '/path/to/node'

set nocompatible 


filetype plugin indent on    " required
let mapleader=" "
syntax on
set nocompatible
filetype off
filetype indent on
filetype plugin on
filetype plugin indent on
set encoding=utf-8
set mouse=v
let &t_SI = "\<Esc>]50;CursorShape=1\x7"
let &t_SR = "\<Esc>]50;CursorShape=2\x7"
let &t_EI = "\<Esc>]50;CursorShape=0\x7"
set list    
set listchars=tab:▸\ ,trail:▫
set number
set cursorline
set cursorcolumn 
highlight CursorLine   cterm=NONE ctermbg=black ctermfg=green guibg=NONE guifg=NONE
set norelativenumber
set wrap
set showcmd
set wildmenu
set hlsearch
exec "nohlsearch"
set incsearch
set autoindent
set smartindent
set completeopt=longest,menu
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif





noremap <LEADER><CR> :nohlsearch<CR>

map s <nop>
map S :w<CR>
map R :source $MYVIMRC<CR>
map Q :q<CR>
map si :set splitright<CR>:vsplit<CR>
map sn :set nosplitright<CR>:vsplit<CR>
map su :set nosplitbelow<CR>:split<CR>
map se :set splitbelow<CR>:split<CR>
map sv <C-w>t<C-w>H
map sh <C-w>t<C-w>K
map <LEADER>o <C-w>l
map <LEADER>i <C-w>k
map <LEADER>y <C-w>h
map <LEADER>u <C-w>j
map <up> :res +5<CR>
map <down> :res -5<CR>
map <left> :vertical resize-5<CR>
map <right> :vertical resize+5<CR>


call plug#begin('~/.vim/plugged')

  Plug 'vim-airline/vim-airline'
  Plug 'connorholyday/vim-snazzy'
  Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
  Plug 'Xuyuanp/nerdtree-git-plugin'
  Plug 'nathanaelkane/vim-indent-guides'
  Plug 'itchyny/vim-cursorword'
  Plug 'octol/vim-cpp-enhanced-highlight'
  Plug 'w0rp/ale'
  Plug 'morhetz/gruvbox'
  "Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

let g:SnazzyTransparent = 1
colorscheme snazzy

" ===
" === NERDTree
" ===
map tt :NERDTreeToggle<CR>
let NERDTreeMapOpenExpl = ""
let NERDTreeMapUpdir = "p"
let NERDTreeMapUpdirKeepOpen = "l"
let NERDTreeMapOpenSplit = ""
let NERDTreeOpenVSplit = ""
let NERDTreeMapActivateNode = "i"
let NERDTreeMapOpenInTab = "o"
let NERDTreeMapPreview = ""
let NERDTreeMapCloseDir = "n"
let NERDTreeMapChangeRoot = "y"


" TextEdit might fail if hidden is not set.
set hidden

" Some servers have issues with backup files, see #649.
set nobackup
set nowritebackup

" Give more space for displaying messages.
set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved.
if has("patch-8.1.1564")
  " Recently vim can merge signcolumn and number column into one
  set signcolumn=number
else
  set signcolumn=yes
endif

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction


" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current
" position. Coc only does snippet and additional edit on confirm.
" <cr> could be remapped by other vim plugin, try `:verbose imap <CR>`.
if exists('*complete_info')
  inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"
else
  inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
endif

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>
