" system-wide defaults are set in $VIMRUNTIME/archlinux.vim (usually just
" /usr/share/vim/vimfiles/archlinux.vim) and sourced by the call to :runtime
" you can find below.  If you wish to change any of those settings, you should
" do it in this file (/etc/vimrc), since archlinux.vim will be overwritten
" everytime an upgrade of the vim packages is performed.  It is recommended to
" make changes after sourcing archlinux.vim since it alters the value of the
" 'compatible' option.

" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages.
runtime! archlinux.vim

" If you prefer the old-style vim functionalty, add 'runtime! vimrc_example.vim'
" Or better yet, read /usr/share/vim/vim80/vimrc_example.vim or the vim manual
" and configure vim to your own liking!

" do not load defaults if ~/.vimrc is missing
"let skip_defaults_vim=1

:filetype plugin on
:syntax on

let skip_defaults_vim=1
let g:powerline_pycmd="py3" 
let g:lightline = {
      \ 'colorscheme': 'jellybeans',
      \ }
"icon
let g:NERDTreeDisableFileExtensionHighlight = 1
let g:NERDTreeDisableExactMatchHighlight = 1
let g:NERDTreeDisablePatternMatchHighlight = 1

let g:NERDTreeFileExtensionHighlightFullName = 1
let g:NERDTreeExactMatchHighlightFullName = 1
let g:NERDTreePatternMatchHighlightFullName = 1

let g:NERDTreeHighlightFolders = 1
let g:NERDTreeHighlightFoldersFullName = 1 
"golang
let g:go_highlight_functions = 1
let g:go_highlight_methods = 1
let g:go_highlight_structs = 1

set rtp+=/usr/lib/python3.6/site-packages/powerline/bindings/vim
:set laststatus=2
":set number"行番号

scriptencoding utf-8
set encoding=utf-8
set t_Co=256
set incsearch
set smartcase
set guifont=Ricty\ Discord\ 12
set guifontwide=Ricty\ Discord\ 12
set matchpairs& matchpairs+=<:>
set shiftround


"Plugin
call plug#begin('path/to/vim/plugins/directory')
"Plug 'powerline/powerline' Powerline もう使わない
Plug 'itchyny/lightline.vim' "Lightline
Plug 'gosukiwi/vim-atom-dark'
Plug 'tomasr/molokai'
Plug 'jkaving/intellij-colors-solarized'
Plug 'liuchengxu/space-vim-dark'
Plug 'cohama/lexima.vim'
Plug 'fatih/vim-go' "go言語
Plug 'fatih/vim-go', {
            \ 'autoload' : { 'filetypes' : 'go'  }
            \ }
Plug 'tiagofumo/vim-nerdtree-syntax-highlight' "fileicon 2
"Plug 'ryanoasis/vim-devicons' "fileicon
Plug 'scrooloose/nerdtree' "ディレクトリツリー
call plug#end()

map <C-n> :NERDTreeToggle<CR>

"カラースキーム”
syntax enable
colorscheme molokai
set background=dark
highlight Normal ctermbg=none
