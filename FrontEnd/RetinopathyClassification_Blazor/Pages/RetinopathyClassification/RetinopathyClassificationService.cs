using Microsoft.JSInterop;
using System.Threading.Tasks;

namespace RetinopathyClassification_Blazor.Pages.RetinopathyClassification
{
    public class RetinopathyClassificationService : IRetinopathyClassificationService
    {
        private readonly IJSRuntime _jsRuntime;

        private const string BaseUrl = "http://127.0.0.1:8080";
        private readonly string ClassificationUrl = $"{BaseUrl}/predict_processed";

        private const string JsLibraryName = "methods";
        private readonly string ReadFileJsFunctionName = $"{JsLibraryName}.readFileAsBase64";

        public RetinopathyClassificationService(IJSRuntime jsRuntime)
        {
            this._jsRuntime = jsRuntime;
        }

        public async Task SetPicture(string inputId, string selectedImageId, RetinopathyClassificationPageCode foodClassificationPageCode)
        {
            await _jsRuntime.InvokeAsync<string>(ReadFileJsFunctionName, inputId, selectedImageId, ClassificationUrl, DotNetObjectReference.Create(foodClassificationPageCode));
        }
    }
}
