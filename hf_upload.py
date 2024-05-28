from huggingface_hub import create_repo
from huggingface_hub import Repository
 
REPO_NAME="merged_slerp_13b"
LOCAL_DIR_NAME="./merged"
NAMESPACE="Yerim"

# Repository 생성
# create_repo(name=REPO_NAME)

repo = Repository(LOCAL_DIR_NAME, clone_from=f"{NAMESPACE}/{REPO_NAME}")

# Repository 삭제
# delete_repo(name=REPO_NAME)

repo.git_pull()
# repo.git_add()
# repo.git_commit('Initial commit')
# repo.git_push()