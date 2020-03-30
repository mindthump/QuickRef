FROM python:alpine
LABEL Author="github.com/mindthump"

# for my own convenience when ssh-ing to instances
RUN apk update \
    && apk add git curl zsh stow tmux vim less mc tree httpie

RUN curl -Lo omz-install.sh https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh \
    && CHSH=no RUNZSH=no sh omz-install.sh -—unattended \
    && rm -f ~/.zshrc omz-install.sh \
    && git clone https://github.com/mindthump/dotfiles.git ~/.dotfiles \
    && stow --dir ~/.dotfiles --stow zsh

ENV APPDIR="/app"

WORKDIR ${APPDIR}

COPY requirements.txt .
#RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY src src
COPY tests tests
