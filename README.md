# github_action_exp
action的實驗筆記

## 相關說明

1. github action pro 有 3000 mins 的執行時間，但 windows 是使用時間算 ubuntu 2倍，而 macOS 是 10 倍

## 參考文件

1. https://www.maxlist.xyz/2020/07/29/flask-cicd-action/
2. https://milkmidi.medium.com/%E6%B7%B1%E5%85%A5%E4%BD%86%E4%B8%8D%E6%B7%BA%E5%87%BA-%E5%A6%82%E4%BD%95%E7%94%A8-github-actions-%E8%87%AA%E5%8B%95%E7%99%BC%E4%BD%88-gh-pages-8183464dfe84
3. https://www.linkedin.com/pulse/running-selenium-web-tests-github-actions-moataz-nabil/

## rysnc 
1. https://docs.github.com/en/actions/reference/encrypted-secrets
2. https://github.com/marketplace/actions/install-ssh-key
3. https://stackoverflow.com/questions/63093761/github-action-rsync-setup-keeps-on-failing
4. 記得生成完指令後，要把private key 加入 cat ~/.ssh/github >>~/.ssh/authorized_keys

## selenium 教學
1. https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html

## 排成教學
https://jasonet.co/posts/scheduled-actions/

## 啟動服務
uvicorn main:app --reload --host 0.0.0.0